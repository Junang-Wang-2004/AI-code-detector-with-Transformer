v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
if v2.count(0) == 1:
    v4 = 3
elif v2.count(0) == 2:
    v4 = 6
    for v5 in v2:
        v6 = v3.count(v5)
        v7 = v3.count(v5 - 1)
        if v5 > 0 and v7 - v6 == 2:
            v4 *= 3
        elif v5 > 0 and v7 - v6 == 1:
            v4 *= 2
        v3.append(v5)
elif v2.count(0) == 3:
    v4 = 6
    for v5 in v2:
        v6 = v3.count(v5)
        v7 = v3.count(v5 - 1)
        if v5 > 0 and v7 - v6 == 3:
            v4 *= 3
        elif v5 > 0 and v7 - v6 == 2:
            v4 *= 2
            v4 *= 1
        v3.append(v5)
print(v4 % 1000000007)
