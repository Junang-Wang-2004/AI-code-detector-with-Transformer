v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = 0
for v5 in range(2 ** v1):
    v6 = 0
    v7 = 0
    for v8 in range(v1):
        if v5 >> v8 & 1:
            v6 += v2[v8]
            v7 += v3[v8]
    v9 = v6 - v7
    if v4 < v9:
        v4 = v9
print(v4)
