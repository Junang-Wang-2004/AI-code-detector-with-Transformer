v1, v2 = map(int, input().split())
v3 = []
v4 = []
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v3.append(v6)
    v4.append(v7)
v8 = max(v3)
v9 = []
v4.sort(reverse=True)
v10 = 0
for v11 in v4:
    if v11 < v8:
        break
    v10 += 1
    v2 -= v11
    if v2 <= 0:
        break
if v2 > 0:
    v10 += (v2 + v8 - 1) // v8
print(v10)
