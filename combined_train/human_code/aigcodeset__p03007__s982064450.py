v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
v3 = 0
for v4 in v2:
    if v4 <= 0:
        v3 += 1
if v3 == v1 or v3 == v1 - 1:
    v5 = v2[-1] - sum(v2[:-1])
    print(v5)
    v4, v6 = (v2[-1], v2[0])
    for v7 in range(1, v1):
        print(v4, v6)
        v4, v6 = (v4 - v6, v2[v7])
elif v3 == 0 or v3 == 1:
    v5 = sum(v2[1:]) - v2[0]
    print(v5)
    v4, v6 = (v2[0], 0)
    for v7 in range(1, v1 - 1):
        v4, v6 = (v4 - v6, v2[v7])
        print(v4, v6)
    v4, v6 = (v2[-1], v4 - v6)
    print(v4, v6)
else:
    v5 = sum(v2[v3:]) - sum(v2[:v3])
    print(v5)
    v4, v6 = (v2[0], 0)
    for v7 in range(v1 - v3 - 1):
        v4, v6 = (v4 - v6, v2[v3 + v7])
        print(v4, v6)
    v4, v6 = (v2[-1], v4 - v6)
    print(v4, v6)
    for v7 in range(v3 - 1):
        v4, v6 = (v4 - v6, v2[v7 + 1])
        print(v4, v6)
