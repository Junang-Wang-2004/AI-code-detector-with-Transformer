from collections import Counter
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1000000007
v4 = Counter()
v4[0] = 3
v5 = 1
for v6 in v2:
    v5 = v5 * v4[v6] % v3
    v4[v6] -= 1
    v4[v6 + 1] += 1
print(v5)
