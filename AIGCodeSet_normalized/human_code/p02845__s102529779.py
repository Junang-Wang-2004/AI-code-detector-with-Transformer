from collections import defaultdict
v1 = 1000000007
v2 = int(input())
v3 = list(map(int, input().split()))
v4 = 1
v5 = defaultdict(int)
for v6 in v3:
    if v6 == 0:
        v4 *= 3 - v5[v6]
        v5[v6] += 1
        continue
    v4 *= v5[v6 - 1] - v5[v6]
    v4 %= v1
    v5[v6] += 1
print(v4)
