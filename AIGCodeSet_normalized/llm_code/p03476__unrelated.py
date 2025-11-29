import math

def f1(a1):
    if a1 <= 1:
        return False
    for v1 in range(2, int(math.sqrt(a1)) + 1):
        if a1 % v1 == 0:
            return False
    return True

def f2(a1, a2):
    v1 = 0
    for v2 in range(a1, a2 + 1, 2):
        if f1(v2) and f1((v2 + 1) // 2):
            v1 += 1
    return v1
v1 = int(input())
for v2 in range(v1):
    v3, v4 = map(int, input().split())
    print(f2(v3, v4))
