v1, v2 = map(int, input().split())
v3 = {}
for v4 in range(v2):
    v5, v6 = input().split()
    v3[v5] = v3.get(v5, []) + [v6]
v7 = {}

def f1(a1):
    if a1 in v7:
        return v7[a1]
    v1 = 0
    for v2 in v3.get(a1, []):
        v1 = max(v1, f1(v2) + 1)
    v7[a1] = v1
    return v7[a1]
v8 = 0
for v9 in range(v1):
    v8 = max(v8, f1(v9))
return v8
