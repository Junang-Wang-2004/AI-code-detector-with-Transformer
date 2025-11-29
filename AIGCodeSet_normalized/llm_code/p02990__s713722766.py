import math

def f1(a1, a2):
    return math.factorial(a1) // (math.factorial(a2) * math.factorial(a1 - a2))
v1, v2 = map(int, input().split())
v3 = 10 ** 9 + 7
for v4 in range(1, v2 + 1):
    print(f1(v1 - v2 + 1, v4) * f1(v2 - 1, v4 - 1) % v3)
