v1 = input().split()
v2 = [1]
v3 = []
for v4 in range(int(v1[0])):
    v3.append(int(input()))
    v2.append(v2[v4] * (v4 + 1))
v5 = v3.copy()
v6 = int(v1[1])
v7 = int(v1[2])
v8 = 0
v9 = 0
v10 = v5.count(max(v5))
while v9 < v6:
    v8 += max(v3)
    v3.remove(max(v3))
    v9 += 1
print(v8 / v6)
v11 = 1
v12 = 0
while v6 >= v10:
    v12 += v10
    v6 = v6 - v10
    for v4 in range(v10):
        v5.remove(max(v5))
    v10 = v5.count(max(v5))
if v10 > v6 and v6 > 0:
    v11 = 0
    v13 = int(v1[1])
    while min(v7, v12 + v10) >= v13:
        v6 = v13
        while v6 <= v13:
            v11 += v2[v10] // (v2[v6] * v2[v10 - v6])
            v6 += 1
        v13 += 1
print(v11)
