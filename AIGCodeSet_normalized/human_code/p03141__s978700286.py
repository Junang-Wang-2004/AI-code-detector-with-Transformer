v1 = int(input())
v2 = []
for v3 in range(v1):
    v4, v5 = map(int, input().split())
    v2.append((v4 + v5, v4, v5))
v2.sort()
v2.reverse()
v6 = 0
for v3 in range(v1):
    if v3 % 2 == 0:
        v6 += v2[v3][1]
    else:
        v6 -= v2[v3][2]
print(v6)
