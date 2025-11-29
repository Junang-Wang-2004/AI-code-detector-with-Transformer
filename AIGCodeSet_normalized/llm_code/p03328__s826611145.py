v1, v2 = map(int, input().split())
v3 = 0
for v4 in range(1, 499500):
    v3 += v4
    if v3 > v1:
        print(v4 - (v3 - v1))
        break
    elif v3 == v1 and v3 <= v2:
        print(v4 - (v2 - v3))
        break
