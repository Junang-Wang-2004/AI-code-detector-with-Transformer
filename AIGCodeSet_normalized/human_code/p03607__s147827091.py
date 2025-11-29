import collections
v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = collections.Counter(v2)
v5 = 0
for v6 in v4.values():
    if v6 % 2 == 1:
        v5 += 1
print(v5)
