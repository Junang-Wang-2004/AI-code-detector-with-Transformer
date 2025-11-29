v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 0
v5 = 0
while max(v2) != 0:
    for v6 in range(v1):
        if v2[v6] != 0:
            v4 = v6
            break
    if v4 == v1 - 1:
        v3 += v2[v1 - 1]
        break
    for v6 in range(v4 + 1, v1):
        v5 = v6
        if v2[v6] == 0:
            break
        if v6 == v1 - 1:
            v5 += 1
    v7 = min(v2[v4:v5])
    for v6 in range(v4, v5):
        v2[v6] -= v7
    v3 += v7
print(v3)
