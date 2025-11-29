v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v3.sort()
v4 = []
v4 = [list(map(int, input().split())) for v5 in range(v2)]
v4.sort(key=lambda x: x[1], reverse=True)
v6 = 0
for v7, v8 in v4:
    v9 = v7
    while v6 < v1 and v9 > 0:
        if v3[v6] < v8:
            v3[v6] = v8
            v9 -= 1
        v6 += 1
        if v6 == v1:
            break
print(sum(v3))
