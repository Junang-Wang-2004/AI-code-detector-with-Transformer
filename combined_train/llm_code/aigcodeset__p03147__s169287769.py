v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4, v5 = (0, 0)
while True:
    if v4 > v1 - 1 or v5 > v1 - 1:
        break
    while v4 < v1 and v2[v4] == 0:
        v4 += 1
    if v4 >= v1:
        break
    v5 = v4
    while v5 < v1 and v2[v5] != 0:
        v5 += 1
    v6 = min(v2[v4:min(v5, v1)])
    for v7 in range(v4, min(v5, v1)):
        v2[v7] -= v6
    v3 += v6
    v4 = v5
print(v3)
