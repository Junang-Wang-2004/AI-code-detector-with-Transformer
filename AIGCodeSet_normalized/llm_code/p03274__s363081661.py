import bisect
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = bisect.bisect(v3, 0)
v5 = [0] + v3[:v4][::-1]
v6 = [0] + v3[v4:]
v7 = 10 ** 7
for v8 in range(min(v2 + 1, len(v5))):
    v9 = v2 - v8
    if v9 >= len(v6):
        continue
    v7 = min(v7, 2 * v6[v9] - v5[v8], -2 * v5[v8] + v6[v9])
print(v7)
