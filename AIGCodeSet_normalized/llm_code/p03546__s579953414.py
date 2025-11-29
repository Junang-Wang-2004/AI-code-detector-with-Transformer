v1, v2 = map(int, input().split())
v3 = [[0] * v2 for v4 in range(v1)]
for v5 in range(v1):
    for v6 in range(v2):
        v3[v5][v6] = int(input())

def f1(a1, a2):
    if a1 == v1 and a2 == v2:
        return 0
    if a1 == v1:
        return f1(0, a2 + 1)
    if a2 == v2:
        return f1(a1 + 1, 0)
    return min(f1(a1, a2 + 1), f1(a1 + 1, a2))
print(f1(0, 0))
