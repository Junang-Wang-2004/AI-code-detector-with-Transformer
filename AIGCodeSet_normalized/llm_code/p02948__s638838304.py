v1, v2 = map(int, input().split())
v3 = [[0, 0] for v4 in range(v1)]
for v4 in range(v1):
    v3[v4][0], v3[v4][1] = map(int, input().split())
    v3[v4].append(v3[v4][1] / v3[v4][0])
v3.sort(reverse=True, key=lambda x: x[1])
v4 = 0
v5 = 0
while v4 < v1 and v2 > 0:
    if v2 >= v3[v4][0]:
        v5 += v3[v4][1]
        v2 -= 1
    v4 += 1
print(v5)
