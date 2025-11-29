v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [tuple(map(int, input().split())) for v5 in range(v2)]
v3.sort(key=lambda x: -x)
v4.sort(key=lambda x: -x[1])
v6 = sum(v3)
v7 = v6
v5 = v1 - 1
v8 = 0
while v5 >= 0:
    if v8 >= v2:
        break
    for v9 in range(v4[v8][0]):
        if v5 < 0:
            break
        v6 -= v3[v5]
        v6 += v4[v8][1]
        v7 = max(v7, v6)
        v5 -= 1
    v8 += 1
print(v7)
