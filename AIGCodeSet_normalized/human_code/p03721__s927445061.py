v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v3.sort()
v5 = 0
for v6 in range(v1):
    v5 += v3[v6][1]
    if v5 >= v2:
        print(v3[v6][0])
        break
