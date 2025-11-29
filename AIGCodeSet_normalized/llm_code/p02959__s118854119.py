def f1(a1, a2):
    if a1 >= a2:
        return a2
    else:
        return a2 - a1
v1 = int(input())
v2 = list(map(int, input().rstrip().split()))
v3 = list(map(int, input().rstrip().split()))
v4 = 0
v5 = 0
v6 = 0
for v7 in range(v1):
    v5 = f1(v2[v7], v3[v7])
    v4 += v5
    if v7 < v1 - 1:
        v3[v7 + 1] = max(0, v3[v7 + 1] - v6)
    v6 = v5
v5 = f1(v2[v1], v3[v1 - 1] if v1 > 0 else 0)
v4 += v5
print(v4)
