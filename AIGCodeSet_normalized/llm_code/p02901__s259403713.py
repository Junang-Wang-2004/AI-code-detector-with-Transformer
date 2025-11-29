import copy
v1, v2 = map(int, input().split())

def f1(a1):
    return int(a1) - 1
v3 = []
v4 = []
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    v3.append(v6)
    v4.append(list(map(f1, input().split())))

def f2(a1, a2, a3):
    """
    初期値
    cost = 0
    still_closed = [1]*N
    d = 0
    """
    if a3 == v2:
        if sum(a2) == 0:
            return a1
        else:
            return -1
    v1 = copy.copy(a2)
    v2 = copy.copy(a2)
    v3 = f2(a1, v1, a3 + 1)
    for v4 in v4[a3]:
        a2[v4] = 0
    v5 = f2(a1 + v3[a3], a2, a3 + 1)
    if v3 == -1 or v5 == -1:
        return max(v3, v5)
    else:
        return min(v3, v5)
print(f2(0, [1] * v1, 0))
