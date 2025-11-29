v1 = int(input())
for v2 in range(v1 + 10):
    if v2 * (v2 + 1) // 2 >= v1:
        break
v3 = list(range(1, v2 + 1))
v4 = v2 * (v2 + 1) // 2 - v1
for v5 in v3:
    if v5 != v4:
        print(v5)
