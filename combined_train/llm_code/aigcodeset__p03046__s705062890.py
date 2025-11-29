def f1(a1, a2):
    return a1 ^ a2

def f2(a1, a2):
    v1 = 1 << a1 + 1
    v2 = [0] * v1
    v3 = [False] * (1 << a1)
    for v4 in range(v1 // 2):
        for v5 in range(1 << a1):
            if not v3[v5]:
                v2[2 * v4] = v5
                v2[2 * v4 + 1] = v5 ^ a2
                v3[v5] = True
                break
    if all(v3):
        return v2
    else:
        return [-1]
v1, v2 = map(int, input().split())
v3 = f2(v1, v2)
if v3 == [-1]:
    print(-1)
else:
    for v4 in v3:
        print(v4, end=' ')
