v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v1):
    v4.append(int(input()))
v6 = 0
v7 = v1
while v7 > 0:
    v8 = 0
    for v5 in range(v7):
        if v4[v5] >= 0:
            v4[v5] -= v3
    v4[v8] -= v2 - v3
    if v4[v8] < v4[v5]:
        v8 = v5
    while v7 > 0 and v4[v7 - 1] <= 0:
        v7 -= 1
    v6 += 1
print(v6)
