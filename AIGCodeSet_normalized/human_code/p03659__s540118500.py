v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = sum(v2)
v5 = []
for v6 in v2[:-1]:
    v3 += v6
    v7 = abs(v4 - 2 * v3)
    v5.append(v7)
v5.sort()
print(v5[0])
