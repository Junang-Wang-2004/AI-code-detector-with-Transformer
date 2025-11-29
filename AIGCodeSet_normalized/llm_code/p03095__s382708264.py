import collections
v1 = 10 ** 9 + 7
v2 = int(input())
v3 = list(input())
v4 = list(collections.Counter(v3).values())
v5 = 1
for v6 in v4:
    if v6 == 1:
        v5 *= 2 % v1
    else:
        v5 *= v6 + 1 % v1
print(v5 - 1)
