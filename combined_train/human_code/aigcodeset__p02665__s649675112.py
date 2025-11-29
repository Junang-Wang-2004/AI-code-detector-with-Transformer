from math import log2
v1 = int(input())
v2 = list(map(int, input().split()))
if v1 == 0:
    if v2[0] == 1:
        print(1)
    else:
        print(-1)
    exit()
if v2[0] != 0:
    print(-1)
    exit()
v2.reverse()
v3 = [None] * (v1 + 1)
for v4, v5 in enumerate(v2):
    if v4 == 0:
        v3[0] = (v5, v5)
        continue
    v3[v4] = (v3[v4 - 1][0] + v5, (v3[v4 - 1][1] + 1) // 2 + v5)
if v3[-1][1] > 1:
    print(-1)
    exit()
v3.reverse()
v6 = 0
v7 = 1
for v4, v8 in enumerate(v3):
    v7 = min(v7, v8[0])
    v6 += v7
    v7 -= v2[v1 - v4]
    v7 *= 2
print(v6)
