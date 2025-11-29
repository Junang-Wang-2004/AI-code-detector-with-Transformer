from collections import defaultdict

def f1(a1, a2, a3, a4):
    for v1 in a3[a1]:
        if v1 != a2:
            a4[v1] = a4[a1] + 1
            if not f1(v1, a1, a3, a4):
                return False
            if a4[v1] % 2 != 0:
                return False
    return True

def f2(a1, a2, a3):
    v1 = defaultdict(list)
    for v2, v3 in a3:
        v1[v2].append(v3)
        v1[v3].append(v2)
    v4 = [0] * (a1 + 1)
    if not f1(1, 0, v1, v4):
        return 'NO'
    if a2 % 2 != 0:
        return 'NO'
    return 'YES'
v1, v2 = map(int, input().split())
v3 = [tuple(map(int, input().split())) for v4 in range(v2)]
print(f2(v1, v2, v3))
