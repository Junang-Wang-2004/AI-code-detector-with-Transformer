v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v3.append([v5, v6])
v3.sort()
for v7 in v3:
    v2 -= v7[1]
    if v2 <= 0:
        print(v7[0])
        break
