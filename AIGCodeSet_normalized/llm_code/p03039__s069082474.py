from math import factorial
v1 = 10 ** 9 + 7

def f1(a1, a2):
    return factorial(a1) % v1 // factorial(a2) % v1 // factorial(a1 - a2) % v1
v2, v3, v4 = map(int, input().split())
print((pow(v3, 2, v1) * f1(v2 * v3 - 2, v4 - 2) * sum(((v2 - i) * i % v1 for v5 in range(1, v2))) % v1 + pow(v2, 2, v1) * f1(v2 * v3 - 2, v4 - 2) * sum(((v3 - v5) * v5 % v1 for v5 in range(1, v3))) % v1) % v1)
