# Python 에서 C 모듈을 사용하는 방법

- 파이썬에서 C/C++ 모듈를 사용하는 방법
- [예제 블로그 1](https://kukuta.tistory.com/374)
- [예제 블로그 2](https://doitnow-man.tistory.com/57)





### 방법

---

#### 필요 파일

- 모듈화를 위한 C 파일
- C모듈을 사용하기 위한 python 파일
- C모듈을 컴파일하고 설치하기 위한 setup.py 파일



#### C 파일 작성

- 파이썬에서 사용하는 C 모듈은 리눅스에서는 `.so` 확장자 형태로, 윈도우에서는 `.pyd` 형태로 빌드되어 파이썬 패키지 디렉토리의  Lib/site-package 디렉토리로 복사되어 사용 가능하게 된다.
  - C로 소스코드를 작성한다.
  - 작성한 C 소스코드를 컴파일하여 파이썬이 이용가능한 `.so` 및 `.pyd` 파일로 빌드한다.
  - 해당 파일을 파이썬 디렉토리의 Lib/site-package로 복사한다.



### 예제 코드(예제 블로그 1) 

---

- 동적 라이브러리를 만들어 줘야하는데 리눅스에서는 so를, 윈도우에서는 dll 을 만들어야 한다. (여기서는 리눅스를 다룸)



#### C/C++ 모듈 작성

```c++
// file : c_module_main.cpp

#define EXPORT                       // 리눅스의 경우 별다른 지정자가 필요치 않다
#endif

#include <vector>
#include <numeric>

extern "C"
{
    // 1. int 타입 인자를 받고, int 타입을 리턴하는 예
    EXPORT int add(int a, int b)
    {
        return a + b;
    }

    // 2. out 파라메터로 포인터를 사용하는 예
    EXPORT void sub(double a, double b, double* result)
    {
        *result = a - b;
    }

    // 3. 배열 파라메터를 사용하는 예
    EXPORT int accumulate(int* input, int size)
    {
        std::vector<int> v(input, input + size);
        int result = std::accumulate(v.begin(), v.end(), 0u);
        return result;
    }

    struct Rect
    {
        int x;
        int y;
        int width;
        int height;
    };

    // 4. 구조체 파라메터를 사용하는 예
    EXPORT int getarea(Rect* r)
    {
        return r->width * r->height;
    }
}
```



#### .so 만들기

```cmd
g++ -shared -fPIC -o libc_module.so ./c_module_main.cpp

#g++ -shared -fPIC -o <동적 라이브러리 이름>.so ./<컴파일 대상 파일 이름>.cpp
```



#### 파이썬에서 C/C++ 동적 모듈 사용

```python
# -*- coding: utf-8 -*-
import ctypes                           # 파이썬 extension을 사용하기 위한 모듈
import platform                         # 파이썬 아키텍처를 확인하기 위한 모듈


### 모듈 로드 ###
if 'Windows' == platform.system() :     # 윈도우 운영체제에서 c 모듈 로드
    path = './x64/Debug/c_module.dll'
    c_module = ctypes.windll.LoadLibrary(path)
elif 'Linux' == platform.system() :     # 리눅스 운영체제에서 c 모듈 로드
    path = "./libc_module.so"
    c_module = ctypes.cdll.LoadLibrary(path)
else :
    raise OSError()
### ###
    
    
# 1. int 타입 인자를 받고, int 타입을 리턴하는 예
add = c_module.add
add.argtypes = (ctypes.c_int, ctypes.c_int)
add.restype = ctypes.c_int

res = add(1, 2)
print(res)

# 2. out 파라메터로 포인터를 사용하는 예
sub = c_module.sub
sub.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double))
sub.restype = None
outparam = ctypes.c_double()

sub(3.2, 2.2, outparam)
print(outparam.value)

# 3. 배열 파라메터를 사용하는 예
accumulate = c_module.accumulate
accumulate.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
accumulate.restype = ctypes.c_int

s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = (ctypes.c_int * len(s))(*s)

res = accumulate(arr, len(s))
print(res)

# 4. 구조체 파라메터를 사용하는 예
class Rect(ctypes.Structure) :
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('width', ctypes.c_int),
        ('height', ctypes.c_int)
    ]

getarea = c_module.getarea
getarea.argtypes = ctypes.POINTER(Rect),
getarea.restype = ctypes.c_int

r = Rect(0, 0, 5, 10)
res = getarea(r)
print(res)
```

