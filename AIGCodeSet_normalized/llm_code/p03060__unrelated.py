v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = 0
for v5 in range(1 << v1):
    v6 = 0
    v7 = 0
    for v8 in range(v1):
        if v5 >> v8 & 1:
            v6 += v2[v8]
            v7 += v3[v8]
    v4 = max(v4, v6 - v7)
print(v4)
