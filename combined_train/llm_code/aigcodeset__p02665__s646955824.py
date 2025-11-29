v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
if v2[0] != 0:
    v3 = 1
else:
    v4 = [1]
    for v5 in range(v1 - 1):
        v6 = 2 * v4[v5] - v2[v5 + 1]
        if v6 <= 0:
            v3 = 1
            break
        v4.append(v6)
    v7 = v2
    for v5 in range(v1 - 1):
        if v7[-(v5 + 1)] + v2[-(v5 + 2)] <= v4[-(v5 + 1)]:
            v7[-(v5 + 2)] = v7[-(v5 + 1)] + v2[-(v5 + 2)]
        elif v4[-(v5 + 2)] < v4[-(v5 + 1)] + v2[-(v5 + 2)] <= v4[-(v5 + 2)] * 2:
            v7[-(v5 + 2)] = v4[-(v5 + 1)] + v2[-(v5 + 2)]
        else:
            v3 = 1
            break
if v3 == 1:
    print(-1)
else:
    v8 = 0
    for v5 in v7:
        v8 += v5
    print(v8 + 1)
