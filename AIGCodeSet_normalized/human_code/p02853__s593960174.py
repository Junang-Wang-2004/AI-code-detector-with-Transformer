v1, v2 = map(int, input().split())
v3 = [0]
v4 = {1: 300000, 2: 200000, 3: 100000}
if v1 in v4:
    v3.append(v4[v1])
if v2 in v4:
    v3.append(v4[v2])
if v1 == 1 and v2 == 1:
    v3.append(400000)
print(sum(v3))
