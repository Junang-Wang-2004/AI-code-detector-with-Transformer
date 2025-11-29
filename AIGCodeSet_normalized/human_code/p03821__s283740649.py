v1 = int(input())
v2 = 0
v3 = [list(map(int, input().split())) for v4 in range(v1)]
for v4 in range(v1)[::-1]:
    if (v3[v4][0] + v2) % v3[v4][1] != 0:
        v2 += v3[v4][1] - (v3[v4][0] + v2) % v3[v4][1]
print(v2)
