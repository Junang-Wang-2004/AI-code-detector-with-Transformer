from collections import Counter
v1 = int(input())
v2 = Counter(list(input()))
v3 = v2.values()
v4 = 1
for v5 in v3:
    v4 *= v5 + 1
    v4 %= 10 ** 9 + 7
print(v4 - 1)
