v1 = int(input())
v2 = list(map(int, input().split()))
v3 = v2[:]
v3.sort()
v4 = int(v1 / 2)
v5 = int((v1 - 2) / 2)
v6 = v3[v5]
v7 = v3[v4]
for v8 in range(v1):
    if v2[v8] <= v6:
        print(v7)
    else:
        print(v6)
