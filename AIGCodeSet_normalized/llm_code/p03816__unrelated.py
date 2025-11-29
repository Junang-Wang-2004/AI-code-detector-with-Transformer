from collections import Counter
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = Counter(v2)
v4 = 0
for v5 in v3.values():
    v4 += min(v5, 2)
print(v4 - 1)
