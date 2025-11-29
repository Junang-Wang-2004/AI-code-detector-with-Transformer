v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v3.sort()
v4 = [-1] * (2 * v1)
v5 = []
for v6 in range(v2):
    v7, v8 = map(int, input().split())
    v5.append((v8, v7))
v5.sort(reverse=True)
v6 = 0
for v9 in range(v2):
    if v6 >= v1:
        break
    for v10 in range(v5[v9][1]):
        v4[v6] = v5[v9][0]
        v6 += 1
v9 = 0
for v6 in range(v1):
    if v3[v6] < v4[v9]:
        v3[v6] = v4[v9]
        v9 += 1
print(sum(v3))
