v1, v2 = list(map(int, input().split()))
v3 = [0, 300000, 200000, 100000] + [0 for v4 in range(10000)]
if v1 == 1 and v2 == 1:
    print(300000 * 2 + 400000)
else:
    print(v3[v1] + v3[v2])
