from collections import Counter
v1 = int(input())
v2 = Counter(list(map(int, input().split())))
v3 = 0
for v4, v5 in v2.items():
    v3 += max(0, v5 - v4)
print(v3)
