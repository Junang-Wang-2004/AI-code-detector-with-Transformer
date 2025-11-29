import itertools
import bisect
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
print(bisect.bisect_right(list(itertools.accumulate(v3)), v2) + 1)
