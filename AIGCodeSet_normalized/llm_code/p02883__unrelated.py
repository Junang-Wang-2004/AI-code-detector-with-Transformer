def f1(a1, a2, a3, a4):
    a3.sort()
    a4.sort(reverse=True)
    v1 = 0
    for v2 in range(a1):
        v1 = max(v1, (a3[v2] - min(a2, v2)) * a4[v2])
    return v1
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
print(f1(v1, v2, v3, v4))
