import collections
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = collections.Counter(v2)
for v4 in range(1, v1 + 1):
    print(v3[v4])
