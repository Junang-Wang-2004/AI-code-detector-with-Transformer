v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5 = list(map(int, input().strip().split()))
    v3.append(v5)
v6 = []
for v4 in range(1, v1 + 1):
    if len(v6) == v2:
        break
    else:
        for v7 in range(v3[v4 - 1][1]):
            v6.append(v3[v4 - 1][0])
            if len(v6) == v2:
                break
v6.sort()
print(v6[v2 - 1])
