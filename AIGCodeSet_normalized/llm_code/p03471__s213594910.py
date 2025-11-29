v1, v2 = map(lambda x: int(x), input().split(' '))
v2 /= 1000
v3 = 10 * v1
if v3 < v2:
    print(-1, -1, -1)
    exit(0)
elif v2 == v3:
    print(v1, 0, 0)
    exit(0)
v4 = v3 - v2
for v5 in range(0, int(v4 / 9) + 1):
    v6 = v4 - 9 * v5
    if v6 % 5 == 0:
        v7 = int(v6 / 5)
        if v1 - v7 - v5 > 0:
            print(v1 - v7 - v5, v7, v5)
            exit(0)
print(-1, -1, -1)
