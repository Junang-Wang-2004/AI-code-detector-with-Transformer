v1 = int(input())
v2 = [int(i) for v3 in input().split()]
v4 = sorted(v2)
v5 = v4[v1 // 2 - 1]
v6 = v4[v1 // 2]
for v7 in v2:
    if v7 >= v6:
        print(v5)
    else:
        print(v6)
