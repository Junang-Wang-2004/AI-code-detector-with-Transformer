v1 = int(input())
v2 = [[int(i) for v3 in input().split()] for v3 in range(v1)]
for v3 in range(v1 - 1):
    if v2[v3][0] > v2[v3 + 1][0] or v2[v3][1] > v2[v3 + 1][1]:
        v4 = (v2[v3][0] - v2[v3][0] % v2[v3 + 1][0]) // v2[v3 + 1][0] + 1
        v5 = (v2[v3][1] - v2[v3][1] % v2[v3 + 1][1]) // v2[v3 + 1][1] + 1
        if v2[v3][0] % v2[v3 + 1][0] == 0:
            v4 -= 1
        if v2[v3][1] % v2[v3 + 1][1] == 0:
            v5 -= 1
        v2[v3 + 1] = [v2[v3 + 1][0] * max(v4, v5), v2[v3 + 1][1] * max(v4, v5)]
print(v2[-1][0] + v2[-1][1])
