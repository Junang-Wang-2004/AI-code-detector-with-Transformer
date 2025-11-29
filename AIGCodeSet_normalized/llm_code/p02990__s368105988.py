import math
v1, v2 = map(int, input().split())

def f1(a1, a2):
    return math.factorial(a1) // math.factorial(a1 - a2)

def f2(a1, a2):
    return f1(a1, a2) // math.factorial(a2)
for v3 in range(1, v2 + 1):
    sum = f2(v1 - v2 + v3, v3) * f2(v2 - 1, v3 - 1)
    print(sum % (10 ** 9 + 7))
