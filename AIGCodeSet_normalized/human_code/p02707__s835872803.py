v1 = int(input())
import sys
input = sys.stdin.readline
v2 = {}
v3 = list(map(int, input().split()))
for v4 in range(v1 - 1):
    v5 = v3[v4]
    if v5 in v2:
        v2[v5] += 1
    else:
        v2[v5] = 1
for v4 in range(1, v1 + 1):
    if v2.get(v4) == None:
        print(0)
    else:
        print(v2.get(v4))
