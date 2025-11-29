import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10 ** 9))
v1 = lambda x: sys.stdout.write(x + '\n')
v2, v3 = list(map(int, input().split()))
v4 = [tuple(map(int, input().split())) for v5 in range(v3)]
from heapq import heappop as hpp, heappush as hp
v6 = []
for v7, (v8, v9) in enumerate(v4):
    hp(v6, (v8, v7, 0))
v10 = 0
v3 = -1
while v6:
    v11, v12, v13 = hpp(v6)
    if v13 == 0:
        hp(v6, (v4[v12][1], v12, 1))
    elif v3 >= 0 and v4[v12][0] <= v3 < v11:
        pass
    else:
        v3 = v4[v12][1] - 1
        v10 += 1
print(v10)
