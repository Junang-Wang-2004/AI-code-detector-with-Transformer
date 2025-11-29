v1 = int(input())
v2 = list(map(int, input().split()))
v3 = sorted(v2)
for v4 in v2:
    v5 = v3.index(v4)
    if v5 < v1 // 2:
        print(v3[v1 // 2 - 1])
    else:
        print(v3[v1 // 2])
