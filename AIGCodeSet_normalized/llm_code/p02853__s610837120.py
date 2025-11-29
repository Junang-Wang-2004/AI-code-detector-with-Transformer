v1, v2 = map(int, input().split())
v3 = [300000, 200000, 100000]
v4 = 0
v5 = 0
if v1 <= 3:
    v4 = v3[v1 - 1]
if v2 <= 3:
    v5 = v3[v2 - 1]
print(v4 + v5 + 400000 * (v1 == 1 and v2 == 1))
