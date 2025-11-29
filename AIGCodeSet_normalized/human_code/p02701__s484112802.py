import collections
v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(input())
v4 = collections.Counter(v2)
print(len(v4))
