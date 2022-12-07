import ctypes

a = ctypes.CDLL("./mylib.so")
mul = a.mul
print(mul(11,10))