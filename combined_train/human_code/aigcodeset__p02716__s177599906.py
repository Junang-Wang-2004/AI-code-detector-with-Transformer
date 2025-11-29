v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 0
v5 = 0
if v1 % 2 == 0:
    for v6, v7 in enumerate(v2):
        if v6 % 2 == 0:
            v3 += v7
        else:
            v4 = max(v3, v4 + v7)
    print(max(v3, v4))
else:
    for v6, v7 in enumerate(v2):
        if v6 % 2 == 0:
            if v6 > 0:
                v5 = max(v5 + v7, v4, v3)
            if v6 < v1 - 1:
                v3 += v7
        else:
            v4 = max(v3, v4 + v7)
    print(max(v3, v4, v5))
