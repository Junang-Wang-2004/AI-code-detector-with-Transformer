from collections import defaultdict
v1 = int(input())
v2 = defaultdict(int)
for v3 in range(v1):
    v4 = int(input())
    v2[v4] += 1
v5 = 0
for v3, v6 in v2.items():
    if v6 % 2 == 1:
        v5 += 1
print(v5)
