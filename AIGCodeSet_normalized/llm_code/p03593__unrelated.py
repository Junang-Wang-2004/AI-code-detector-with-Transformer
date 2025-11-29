v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v3.append(input())
from collections import Counter
v5 = Counter()
for v6 in range(v1):
    for v7 in range(v2):
        v5[v3[v6][v7]] += 1
for v8 in v5.values():
    if v8 % 2:
        if v8 > 1:
            print('No')
            exit()
print('Yes')
