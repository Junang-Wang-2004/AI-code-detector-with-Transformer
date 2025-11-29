v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v2.sort(key=lambda x: x[0] - x[1], reverse=True)
v4 = 0
v5 = 0
for v6 in range(v1):
    if v6 % 2 == 0:
        v4 += v2[v6][0]
    else:
        v5 += v2[v6][1]
print(v4 - v5)
