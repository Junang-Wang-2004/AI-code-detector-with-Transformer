v1, v2, *v3 = map(int, open(0).read().split())
v4 = v3[::2]
v5 = max(v4)
v6 = sorted([i for v7 in v3[1::2] if v7 > v5], reverse=1)
v8 = 0
for v7 in v6:
    v8 += 1
    v2 -= v7
    if v2 <= 0:
        break
v8 += (v2 + v5 - 1) // v5
print(v8)
