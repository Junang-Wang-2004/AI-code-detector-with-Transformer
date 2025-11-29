v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split()))[::-1]]
v4 = 0
v5 = 0
for v6 in range(v2):
    if v3[v6][1] >= v5:
        v4 += 1
        v5 = v3[v6][0]
print(v4)
