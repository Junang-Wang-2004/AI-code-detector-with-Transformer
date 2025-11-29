v1 = int(input())
v2, v3 = [int(x) for v4 in input().split()]
v5 = [int(v4) for v4 in input().split()]
v6 = v7 = v8 = 0
for v9 in v5:
    if v9 <= v2:
        v6 += 1
    elif v9 <= v3:
        v7 += 1
    else:
        v8 += 1
print(min(v6, v7, v8))
