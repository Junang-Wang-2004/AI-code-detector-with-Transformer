from collections import defaultdict
import bisect
v1 = input()
v2 = input()
v3 = defaultdict(list)
for v4, v5 in enumerate(v1, 1):
    v3[v5].append(v4)
v6 = 0
v7 = 0
for v8 in v2:
    v9 = v3[v8]
    if len(v9) == 0:
        print(-1)
        quit()
    if v9[-1] <= v6:
        v6 = v9[0]
        v7 += 1
    else:
        v6 = v9[bisect.bisect_right(v9, v6)]
print(len(v1) * v7 + v6)
