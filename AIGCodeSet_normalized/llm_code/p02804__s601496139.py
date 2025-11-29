import math

def f1(a1, a2):
    return math.factorial(a1) // (math.factorial(a2) * math.factorial(a1 - a2))
v1, v2 = map(int, input().split())
v3 = sorted(map(int, input().split()))
v4 = 0
v5 = 0
for v6 in range(v1):
    if v6 >= v2 - 1:
        v5 += v3[v6] * f1(v6, v2 - 1) % (10 ** 9 + 7)
    if v1 - v6 >= v2:
        v4 += v3[v6] * f1(v1 - v6 - 1, v2 - 1) % (10 ** 9 + 7)
v7 = (v5 - v4) % (10 ** 9 + 7)
print(int(v7))
