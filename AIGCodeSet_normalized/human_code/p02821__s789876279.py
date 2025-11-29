from bisect import bisect_left as BL
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v3.sort()

def f1(a1):
    v1 = 0
    for v2 in range(v1):
        v1 += v1 - BL(v3, a1 - v3[v2])
    return v1 >= v2
v4 = 0
v5 = v3[-1] * 2 + 1
v6 = (v4 + v5) // 2
while abs(v4 - v5) > 1:
    v6 = (v4 + v5) // 2
    if f1(v6):
        v4 = v6
    else:
        v5 = v6
v7 = reversed(v3)
v8 = [0]
for v9 in v7:
    v8.append(v9 + v8[-1])
v10 = 0
v11 = 0
for v12 in range(v1):
    v13 = v1 - BL(v3, v4 - v3[v12])
    v11 += v13
    v10 += v3[v12] * v13
    v10 += v8[v13]
v10 -= (v11 - v2) * v4
print(v10)
