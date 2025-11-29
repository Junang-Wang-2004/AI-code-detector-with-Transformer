from bisect import bisect
v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = [1 for v3 in range(v1 + 2)]
for v5 in range(v1):
    v6 = bisect(v4, -v2[v5])
    v4[v6] = -v2[v5]
v7 = 1
while v4[v7] <= 0:
    v7 += 1
print(v7)
