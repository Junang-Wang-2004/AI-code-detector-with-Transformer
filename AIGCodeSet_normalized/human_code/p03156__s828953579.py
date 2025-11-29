v1 = int(input())
v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = 0
v6 = 0
v7 = 0
for v8 in v4:
    if v8 <= v2:
        v5 += 1
    elif v8 >= v2 + 1 and v8 <= v3:
        v6 += 1
    elif v8 >= v3 + 1:
        v7 += 1
print(min(v5, v6, v7))
