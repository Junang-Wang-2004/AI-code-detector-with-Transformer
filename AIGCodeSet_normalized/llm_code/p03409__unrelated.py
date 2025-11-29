import bisect
v1 = int(input())
v2 = sorted([tuple(map(int, input().split())) for v3 in range(v1)])
v4 = sorted([tuple(map(int, input().split())) for v3 in range(v1)])
v5 = 0
for v6, v7 in v4:
    v8 = bisect.bisect_right(v2, (v6, float('inf')))
    v9 = bisect.bisect_right([v7 for v6, v7 in v2[:v8]], v7)
    v5 += v9
    v2 = v2[:v9] + v2[v8:]
print(v5)
