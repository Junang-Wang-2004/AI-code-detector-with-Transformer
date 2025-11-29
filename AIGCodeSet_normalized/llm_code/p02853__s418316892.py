v1, v2 = map(int, input().split())
v3 = {1: 300000, 2: 200000, 3: 100000}
v4 = v3.get(v1, 0) + v3.get(v2, 0)
if v1 == 1 and v2 == 1:
    v4 += 400000
print(v4)
