v1, v2 = map(int, input().split())
v3 = [1]
v4 = [1]
for v5 in range(v1):
    v3.append(v3[-1] * 2 + 1)
    v4.append(v4[-1] * 2 + 3)
v6 = 0
for v5 in range(v1, -1, -1):
    v7 = v4.pop()
    v8 = v3.pop()
    if v2 >= v7 // 2:
        v6 += v8 // 2
        v2 -= v7 // 2
        if v2:
            v6 += 1
    if v2:
        v2 -= 1
print(v6)
