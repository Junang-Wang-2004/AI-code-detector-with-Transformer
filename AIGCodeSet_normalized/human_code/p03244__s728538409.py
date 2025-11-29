from collections import Counter
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = Counter(v2[::2]).most_common()
v4 = Counter(v2[1::2]).most_common()
if v3[0][0] == v4[0][0]:
    if len(v3) == len(v4) == 1:
        v5 = v1 - max(v3[0][1], v4[0][1])
    else:
        v5 = v1 - max(v3[0][1] + v4[1][1], v4[0][1] + v3[1][1])
else:
    v5 = v1 - v3[0][1] - v4[0][1]
print(v5)
