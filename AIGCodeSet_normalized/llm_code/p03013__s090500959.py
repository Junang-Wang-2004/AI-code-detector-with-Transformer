v1, v2 = map(int, input().split())
v3 = list((int(input()) for v4 in range(v2)))
v5 = [0] * (v1 + 1)
v6 = 0
for v4 in range(v1 + 1):
    if v4 in v3[v6]:
        v5[v4] = 0
        v6 += 1
    elif v4 == 0 or v4 == 1:
        v5[v4] = 1
    else:
        v5[v4] = v5[v4 - 1] + v5[v4 - 2]
print(v5[-1] % 1000000007)
