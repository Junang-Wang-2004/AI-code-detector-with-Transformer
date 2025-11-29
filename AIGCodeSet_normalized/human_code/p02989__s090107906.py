v1 = int(input())
v2 = sorted([int(i) for v3 in input().split()])
if v2[v1 // 2 - 1] == v2[v1 // 2]:
    print(0)
else:
    print(v2[v1 // 2] - v2[v1 // 2 - 1])
