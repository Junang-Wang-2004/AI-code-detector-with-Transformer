v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 1
for v5 in range(v1):
    if v2[v5] == v4:
        v4 += 1
    else:
        v3 += 1
if v4 == 1:
    print(-1)
else:
    print(v3)
