import collections
import copy
v1 = int(input())
v2 = ['a']
v3 = [chr(i) for v4 in range(97, 97 + 26)]
for v4 in range(v1 - 1):
    v5 = []
    for v6 in range(len(v2)):
        v7 = collections.Counter(v2[v6])
        for v8 in range(len(v7.values()) + 1):
            v5.append(v2[v6] + v3[v8])
    v2 = copy.copy(v5)
v2.sort()
for v4 in range(len(v2)):
    print(v2[v4])
