v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v1):
    v4.append(int(input()))
v4.sort()
v6 = 0
v7 = 0
while v7 < v1:
    if v4[v7] <= 0:
        v7 += 1
        continue
    v6 += 1
    v4[v7] -= v2
    for v8 in range(v7 + 1, v1):
        v4[v8] -= v3
        if v4[v8] <= 0:
            v7 += 1
            break
print(v6)
