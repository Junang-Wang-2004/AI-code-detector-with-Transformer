v1 = int(input())
v2 = 1
v3 = [int(i) for v4 in input().split()]
for v4 in range(v1):
    if v3[v4] == v2:
        v2 += 1
if v1 == 1 and v2 == 1:
    print(0)
elif v2 == 1:
    print(-1)
else:
    print(v1 - v2 + 1)
