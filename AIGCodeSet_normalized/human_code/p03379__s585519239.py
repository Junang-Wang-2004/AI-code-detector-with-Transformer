v1 = int(input())
v2 = list(map(int, input().split()))
v3 = sorted(v2)
v4 = v3[v1 // 2 - 1]
v5 = v3[v1 // 2]
for v6 in range(v1):
    if v2[v6] <= v4:
        print(v5)
    else:
        print(v4)
