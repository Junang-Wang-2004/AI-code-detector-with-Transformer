v1 = int(input())
v2 = 0
for v3 in range(1, v1 + 1):
    v2 += v3
    if v2 >= v1:
        v4 = v3
        break
v5 = v2 - v1
for v3 in range(1, v4 + 1):
    if v3 == v5:
        continue
    print(v3)
