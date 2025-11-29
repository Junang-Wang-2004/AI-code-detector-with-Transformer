v1, v2 = map(int, input().split())
v3, v4 = ([], [])
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v3.append(v6)
    v4.append(v7)
v3.sort()
v4.sort()
v8, v9 = (0, v3[-1])
for v7 in v4[::-1]:
    if v7 <= v9 or v2 <= 0:
        v10 = (v2 + v9 - 1) // v9
        break
    v2 -= v7
    v8 += 1
print(v8 + v10)
