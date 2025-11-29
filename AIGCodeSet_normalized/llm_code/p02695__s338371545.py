v1, v2, v3 = map(int, input().split())
v4 = [list(map(int, input().split())) for v5 in range(v3)]

def f1(a1):
    v1 = 0
    if len(a1) == v1:
        for v2, v3, v4, v5 in v4:
            if a1[v3 - 1] - a1[v2 - 1] == v4:
                v1 += v5
        return v1
    for v6 in range(a1[-1] if a1 else 1, v2 + 1):
        v1 = max(v1, f1(a1 + [v6]))
    return v1
print(f1([]))
