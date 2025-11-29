v1, v2 = map(int, input().split())
v3 = input()
v4 = 0
for v5 in range(len(v3)):
    if v3[v5] == '1':
        v4 += 1
        if v4 >= v2:
            print(-1)
            exit()
v4 = 0
from collections import defaultdict
v6 = defaultdict(int)
v6[v4] = v1
for v5 in reversed(range(len(v3))):
    if v3[v5] == '1':
        continue
    if v6[v4] - v5 <= v2:
        v6[v4 + 1] = v5
    else:
        v4 += 1
        v6[v4 + 1] = v5
v7 = []
for v5 in reversed(range(len(v6) - 1)):
    v7.append(v6[v5] - v6[v5 + 1])
print(*v7, sep=' ')
