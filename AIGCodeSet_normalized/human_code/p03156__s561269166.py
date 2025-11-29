v1 = int(input())
v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = 0
v4.sort()
v6 = 0
v7 = 0
v8 = 0
for v9 in range(len(v4)):
    if v4[v9] <= v2:
        v6 += 1
    elif v2 < v4[v9] <= v3:
        v7 += 1
    else:
        v8 += 1
print(min(v6, v7, v8))
