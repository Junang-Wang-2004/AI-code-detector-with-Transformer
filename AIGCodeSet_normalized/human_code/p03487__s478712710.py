v1 = 10 ** 5
v2 = [0] * (v1 + 1)
v3 = 0
v4 = int(input())
v5 = list(map(int, input().split()))
for v6 in v5:
    if v6 > v1:
        continue
    v2[v6] += 1
for v7 in range(1, v4 + 1):
    if v2[v7] >= v7:
        v3 += v7
print(v4 - v3)
