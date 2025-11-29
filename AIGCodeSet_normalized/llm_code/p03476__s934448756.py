import math

def f1(a1):
    if a1 < 2:
        return False
    else:
        v1 = math.floor(math.sqrt(a1))
        for v2 in range(2, v1 + 1):
            if a1 % v2 == 0:
                return False
    return True

def f2():
    v1 = []
    v2 = int(input())
    for v3 in range(v2):
        v4 = 0
        v5, v6 = map(int, input().split())
        v7 = v5
        while v7 <= v6:
            if f1(v7) and f1((v7 + 1) / 2):
                v4 += 1
            v7 += 2
        v1.append(str(v4))
    print('\n'.join(v1))
f2()
