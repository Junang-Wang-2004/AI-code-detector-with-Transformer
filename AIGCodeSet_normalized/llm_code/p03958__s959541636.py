import math
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
if v2 == 1:
    print(v1 - 1)
else:
    v4 = math.ceil(v1 / 2)
    v5 = 0
    for v6 in v3:
        if v6 > v4:
            v5 += v6 - v4
    print(v5)
