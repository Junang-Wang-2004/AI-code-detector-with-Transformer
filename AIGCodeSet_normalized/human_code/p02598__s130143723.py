v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 0
v5 = max(v3) + 1
while v5 - v4 > 1:
    v6 = (v4 + v5) // 2
    v7 = 0
    for v8 in range(v1):
        if v3[v8] % v6 == 0:
            v7 += v3[v8] // v6 - 1
        else:
            v7 += v3[v8] // v6
    if v7 > v2:
        v4 = v6
    else:
        v5 = v6
print(v5)
