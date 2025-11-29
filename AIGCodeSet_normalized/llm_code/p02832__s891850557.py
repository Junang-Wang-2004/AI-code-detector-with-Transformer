v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1
v4 = 0
if 1 in v2:
    while v3 in v2[v4:]:
        v4 = v2.index(v3, v4)
        v3 += 1
    print(v1 - v3 + 1)
else:
    print(-1)
