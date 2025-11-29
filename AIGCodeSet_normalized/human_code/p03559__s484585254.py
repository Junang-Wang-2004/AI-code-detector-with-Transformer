v1 = int(input())
v2 = sorted(list(map(int, input().split())))
v3 = list(map(int, input().split()))
v4 = sorted(list(map(int, input().split())))
import bisect
v5 = 0
for v6 in range(v1):
    v7 = bisect.bisect_left(v2, v3[v6])
    v8 = bisect.bisect_right(v4, v3[v6])
    v5 += v7 * (v1 - v8)
print(v5)
