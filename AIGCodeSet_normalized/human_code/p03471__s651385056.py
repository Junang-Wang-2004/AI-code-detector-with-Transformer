v1, v2 = map(int, input().split())
v2 /= 1000
for v3 in range(v1 + 1):
    for v4 in range(v1 - v3 + 1):
        v5 = v1 - v3 - v4
        if 10 * v3 + 5 * v4 + v5 == v2:
            print(v3, v4, v5)
            exit()
print('-1 -1 -1')
