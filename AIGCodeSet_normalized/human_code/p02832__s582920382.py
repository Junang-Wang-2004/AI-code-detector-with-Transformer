v1 = int(input())
v2 = [int(_) for v3 in input().split()]
v4 = 0
for v5 in v2:
    if v5 == v4 + 1:
        v4 = v5
if v4 == 0:
    print(-1)
else:
    print(v1 - v4)
