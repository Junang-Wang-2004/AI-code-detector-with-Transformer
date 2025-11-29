from collections import Counter
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4, v5 in Counter(v2).items():
    if v4 > v5:
        v3 += v5
    else:
        v3 += v5 - v4
print(v3)
