v1, v2 = [int(x) for v3 in input().rstrip().split()]
v4 = 0
for v5 in range(1, 20000):
    v6 = int(0.08 * v5)
    v7 = int(0.1 * v5)
    if v6 == v1 and v7 == v2:
        print(v5)
        v4 = 1
        break
if v4 == 0:
    print(-1)
