from collections import Counter
v1 = 10 ** 9 + 7
v2 = int(input())
v3 = input()
v4 = Counter(v3)
v5 = 1
for v6 in v4.values():
    v5 = v5 * (v6 + 1) % v1
v5 = (v5 - 1) % v1
print(v5)
