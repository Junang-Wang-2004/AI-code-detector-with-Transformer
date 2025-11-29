v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
for v4 in v2:
    v3.append(v4)
v3 = sorted(v3)
v5 = 0
for v4 in range(v1 - 2):
    for v6 in range(v4 + 1, v1 - 1):
        if v3[v4] == v3[v6]:
            continue
        for v7 in range(v6 + 1, v1):
            if v3[v6] == v3[v7]:
                continue
            if v3[v7] < v3[v4] + v3[v6]:
                v5 += 1
print(v5)
