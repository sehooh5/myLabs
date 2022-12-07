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