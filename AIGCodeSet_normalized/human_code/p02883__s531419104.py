v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v3.sort()
v4.sort(reverse=True)
v5 = 10 ** 12
v6 = 0
while abs(v5 - v6) > 4:
    v7 = (v5 + v6) // 2
    v8 = 0
    for v9 in range(v1):
        v10 = 0
        if v3[v9] * v4[v9] > v7:
            v8 += v3[v9] - int(v7 / v4[v9])
            if v8 > v2:
                v10 = 1
                break
    if v10 == 1:
        v6 = v7
    else:
        v5 = v7
for v11 in range(5):
    v12 = v5 - v11
    v8 = 0
    for v9 in range(v1):
        if v3[v9] * v4[v9] > v12:
            v8 += v3[v9] - int(v12 / v4[v9])
            if v8 > v2:
                print(v12 + 1)
                exit()
print(0)
