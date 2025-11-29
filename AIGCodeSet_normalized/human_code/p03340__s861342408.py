v1 = int(input())
v2 = list(map(int, input().split()))
v3, v4 = (0, 0)
v5 = v2[0]
v6 = v2[0]
v7 = 0
while v3 < v1 and v4 < v1:
    if v5 == v6:
        v7 += v4 - v3 + 1
        v4 += 1
        if v4 > v1 - 1:
            break
        v5 += v2[v4]
        v6 ^= v2[v4]
    else:
        v5 -= v2[v3]
        v6 ^= v2[v3]
        v3 += 1
print(v7)
