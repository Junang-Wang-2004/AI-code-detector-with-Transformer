import sys
input = lambda: sys.stdin.readline()
import collections
v1 = int(input())
v2 = sorted(list(map(int, input().split())))
v3 = collections.Counter(v2)
v4 = {}
for v5, v6 in v3.items():
    if v6 > 1:
        v4[v5] = v6
if (sum(list(v4.values())) - len(v4)) % 2 == 0:
    print(len(set(v2)))
else:
    print(len(set(v2)) - 1)
