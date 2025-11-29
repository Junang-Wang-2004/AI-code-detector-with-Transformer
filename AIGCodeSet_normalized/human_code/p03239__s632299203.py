v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v5 = [1001]
for v4 in range(v1):
    if v3[v4][1] <= v2:
        v5 = [min(v5), v3[v4][0]]
print(min(v5)) if min(v5) < 1001 else print('TLE')
