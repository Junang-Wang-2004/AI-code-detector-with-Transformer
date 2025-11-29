import bisect
v1 = int(input())
v2 = sorted(map(int, input().split()))
v3 = sorted(map(int, input().split()))
v4 = sorted(map(int, input().split()))
v5 = 0
for v6 in range(v1):
    v7 = bisect.bisect_right(v3, v4[v6])
    v8 = bisect.bisect_right(v2, v3[v7 - 1]) if v7 > 0 else 0
    v5 += v8 * (v1 - v7)
print(v5)
