import sys
import itertools
v1 = int(input())
v2 = []
for v3 in range(v1):
    v4 = list(map(int, input().split()))
    v2.append(v4)
v5 = list(itertools.permutations(v2, 2))
if v1 == 1:
    print(1)
    sys.exit()
v6 = {}
for v3 in range(len(v5)):
    v7 = v5[v3][1][0] - v5[v3][0][0]
    v8 = v5[v3][1][1] - v5[v3][0][1]
    v6[str(v7) + ',' + str(v8)] = 0
for v3 in range(len(v5)):
    v7 = v5[v3][1][0] - v5[v3][0][0]
    v8 = v5[v3][1][1] - v5[v3][0][1]
v9 = max(v6.values())
v10 = v1 - v9
v11 = max(v6.items(), key=lambda x: x[1])[0]
v7, v8 = map(int, v11.split(','))
print(v10)
