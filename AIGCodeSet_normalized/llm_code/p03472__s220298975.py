v1, v2 = map(int, input().split())
v3 = []
v4 = 0
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v4 = max(v4, v6)
    v3.append(v7)
v3 = sorted([v7 for v7 in v3 if v7 > v4], reverse=True)
v8 = 0
for v7 in v3:
    v2 -= v7
    v8 += 1
    if v2 <= 0:
        break
if v2 > 0:
    v8 += (v2 - 1) // v4 + 1
print(v8)
