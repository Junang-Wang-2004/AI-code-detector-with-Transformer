import math

def f1(a1):
    v1 = int(math.pow(a1, 1 / 5))
    v2 = -v1
    return (v1, v2)
v1 = int(input())
v2, v3 = f1(v1)
print(v2, v3)
