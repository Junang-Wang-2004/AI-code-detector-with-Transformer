v1 = int(input())
v2 = []
for v3 in range(v1):
    v4, v5 = map(int, input().split(' '))
    v2.append([v4 + v5, v4, v5])
v2 = sorted(v2, key=lambda x: x[0])[::-1]
v6 = 0
for v7 in range(v1):
    if v7 % 2 == 0:
        v6 += v2[v7][1]
    else:
        v6 -= v2[v7][2]
print(v6)
