v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v3.sort(key=lambda x: x[1])
v3.sort(reverse=1, key=lambda x: x[0])
v5 = []
v6 = v3[0][0]
v7 = v3[0][1]
for v4 in range(1, v1):
    if v3[v4][1] > v6:
        v5.append(v3[v4][1])
v5.sort(reverse=1)
v8 = 1
v2 -= v7
v4 = 0
while v2 > 0 and v4 <= len(v5) - 1:
    v2 -= v5[v4]
    v8 += 1
    v4 += 1
if v2 > 0:
    v9 = v2 // v6
    v2 -= v9 * v6
    v8 += v9
if v2 > 0:
    v2 -= v6
    v8 += 1
if v2 + v7 <= 0:
    v8 -= 1
print(v8)
