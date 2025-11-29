from collections import Counter
v1 = int(input())
v2 = Counter([int(input()) for v3 in range(v1)])
v4 = 0
for v3 in v2.values():
    v4 += v3 % 2
print(v4)
