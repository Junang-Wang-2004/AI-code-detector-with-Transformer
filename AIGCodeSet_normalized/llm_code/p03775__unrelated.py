import math

def f1(a1):
    v1 = float('inf')
    for v2 in range(1, int(math.sqrt(a1)) + 1):
        if a1 % v2 == 0:
            v3 = a1 // v2
            v1 = min(v1, max(len(str(v2)), len(str(v3))))
    return v1
v1 = int(input())
print(f1(v1))
