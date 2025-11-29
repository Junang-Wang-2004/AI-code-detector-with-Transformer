v1, v2 = map(int, input().split())
if v2 >= pow(2, v1):
    print(-1)
elif v2 == 0:
    v3 = []
    for v4 in range(pow(2, v1)):
        v3.append(v4)
        v3.append(v4)
    print(*v3)
else:
    v5 = 0
    v6 = []
    for v4 in range(pow(2, v1)):
        if v4 == v2:
            continue
        v5 ^= v4
        v6.append(v4)
    if v5 == v2:
        v7 = list(reversed(v6))
        v3 = v6 + [v2] + v7 + [v2]
        print(*v3)
    else:
        print(-1)
