v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1
for v4 in range(v1):
    if v2[v4] == v3:
        v3 += 1
if v3 == 1:
    print(-1)
else:
    print(v1 - v3 + 1)
