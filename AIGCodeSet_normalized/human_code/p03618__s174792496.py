import collections
v1 = input()
v2 = collections.defaultdict(int)
v3 = 1
for v4, v5 in enumerate(v1):
    v3 += v4 - v2[v5]
    v2[v5] += 1
print(v3)
