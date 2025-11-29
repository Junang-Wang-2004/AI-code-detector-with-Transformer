from collections import Counter
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = Counter(v2)
v4 = 0
for v5, v6 in v3.items():
    if v6 >= v5:
        v4 += v6 - v5
    else:
        v4 += v6
print(v4)
