v1 = int(input())
v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = 0
v6 = 0
v7 = 0
for v8 in range(v1):
    if v4[v8] <= v2:
        v5 += 1
    elif v2 < v4[v8] <= v3:
        v6 += 1
    else:
        v7 += 1
v9 = min(v5, v6, v7)
print(v9)
