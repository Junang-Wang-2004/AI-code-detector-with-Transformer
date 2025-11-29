v1 = int(input())
v2 = list(map(int, input().split()))
v3, v4 = (v1 // 2 - 1, v1 // 2)
v5 = sorted(v2)
v6, v7 = (v5[v3], v5[v4])
if v6 == v7:
    for v8 in range(v1):
        print(v6)
else:
    for v9 in range(v1):
        v10 = v2[v9]
        if v10 <= v6:
            print(v7)
        if v10 >= v7:
            print(v6)
