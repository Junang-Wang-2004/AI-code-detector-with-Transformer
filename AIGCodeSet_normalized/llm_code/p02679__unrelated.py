import sys
v1 = 1000000007
v2 = int(input())
v3 = [tuple(map(int, input().split())) for v4 in range(v2)]
v5 = [1] + [0] * v2
for v6 in range(v2):
    for v7 in range(v6):
        if v3[v6][0] * v3[v7][0] + v3[v6][1] * v3[v7][1] == 0:
            v5[v6 + 1] = (v5[v6 + 1] - v5[v7]) % v1
    v5[v6 + 1] = (v5[v6 + 1] + v5[v6]) % v1
print(v5[-1])
