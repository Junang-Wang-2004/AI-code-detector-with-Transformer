import collections
v1 = input()
v2 = collections.Counter(v1)
v3 = len(v1) * (len(v1) - 1) // 2
for v4 in v2.values():
    v3 -= v4 * (v4 - 1) // 2
print(v3 + 1)
