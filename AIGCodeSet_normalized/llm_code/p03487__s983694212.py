import collections
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = collections.Counter(v2)
for v5, v6 in v4.items():
    v3 += v6 % v5
print(v3)
