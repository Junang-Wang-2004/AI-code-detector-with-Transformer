v1, v2 = map(int, input().split())
if v1 == 2:
    v3 = [10000 * i for v4 in range(1, 101)]
    print(v3[v2 - 1] if v2 != 100 else v3[v2])
elif v1 == 1:
    v3 = [100 * v4 for v4 in range(1, 101)]
    print(v3[v2 - 1] if v2 != 100 else v3[v2])
else:
    print(v2 if v2 != 100 else 101)
