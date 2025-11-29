v1 = int(input())
v2 = [v2 for v2 in map(float, input().split())]
v2.sort()
v3 = 0
for v4 in range(v1):
    if v4 == 0 or v4 == 1:
        v3 += v2[v4] / 2 ** (v1 - 1)
    else:
        v3 += v2[v4] / 2 ** (v1 - v4)
print(v3)
