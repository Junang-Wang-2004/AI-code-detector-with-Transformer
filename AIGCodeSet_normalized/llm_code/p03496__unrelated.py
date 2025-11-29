v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
for v4 in range(1, v1):
    if v2[v4] < v2[v4 - 1]:
        v5 = v2[v4 - 1] - v2[v4]
        v2[v4] += v5
        v3.append((v4, v4 + 1))
        for v6 in range(v4 + 1, v1):
            v2[v6] += v5
            v3.append((v4, v6 + 1))
print(len(v3))
for v7 in v3:
    print(*v7)
