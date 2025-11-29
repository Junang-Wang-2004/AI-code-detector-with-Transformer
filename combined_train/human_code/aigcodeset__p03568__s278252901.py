import math
import string

def f1():
    return list(map(int, input().split()))

def f2(a1, a2):
    return math.factorial(a1) // (math.factorial(a1 - a2) * math.factorial(a2))

def f3(a1):
    v1 = []
    for v2 in a1:
        if not v2 in v1:
            v1.append(v2)
    return len(a1) != len(v1)

def f4(a1):
    v1 = []
    for v2 in range(1, a1 + 1):
        if a1 % v2 == 0:
            v1.append(v2)
    return v1
v1 = [-1, -1, -1, 0, 0, 1, 1, 1]
v2 = [-1, 0, 1, -1, 1, -1, 0, 1]
v3 = int(input())
v4 = f1()
sum = 1
for v5 in range(len(v4)):
    if v4[v5] % 2 == 0:
        sum *= 2
    else:
        sum *= 1
print(3 ** len(v4) - sum)
