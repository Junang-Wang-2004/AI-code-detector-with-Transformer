import sys
import bisect
input = sys.stdin.readline
v1 = 0
v2 = int(input())
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v5 = list(map(int, input().split()))
v3.sort()
v4.sort()
v5.sort()
for v6 in v4:
    v7 = bisect.bisect_left(v3, v6)
    v8 = len(v5) - bisect.bisect_right(v5, v6)
    v1 += v7 * v8
print(v1)
