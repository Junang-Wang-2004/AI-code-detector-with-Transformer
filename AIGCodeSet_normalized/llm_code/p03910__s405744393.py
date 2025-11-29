v1 = int(input())
v2 = v1
v3 = [0]
v4 = 0
for v5 in range(1, v2 + 1):
    v4 += v5
    if v4 <= v2:
        v3.append(v4)
    else:
        break
v6 = len(v3)
for v5 in range(v6, 0, -1):
    if v1 >= v5:
        v1 -= v5
        print(v5)
