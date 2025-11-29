from itertools import accumulate
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(accumulate(v2))
v4 = 2 * 10 ** 9
v5 = v3[-1]
for v6 in v3:
    v4 = min(v4, abs(v6 - (v5 - v6)))
print(v4)
