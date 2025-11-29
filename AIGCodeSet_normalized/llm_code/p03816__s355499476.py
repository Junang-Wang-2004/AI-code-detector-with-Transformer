from collections import Counter
v1 = int(input())
v2 = [int(i) for v3 in input().split()]
v4 = Counter(v2)
v5 = len(v4)
v6 = []
for v7 in v4.values():
    if v7 >= 2:
        v6.append(v7)
v8 = sum(v6)
for v9 in v6:
    if v9 > v8 // 2:
        v5 -= v9 - (v8 + 1) // 2
print(v5)
