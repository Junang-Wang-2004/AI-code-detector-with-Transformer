from collections import Counter
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [l for v4, v5 in enumerate(v2) if v4 % 2 == 0]
v6 = [v5 for v4, v5 in enumerate(v2) if v4 % 2 == 1]
v7 = list(set(v3))
v8 = list(set(v6))
if Counter(v3).most_common()[0][0] != Counter(v6).most_common()[0][0]:
    v9 = len(v3) - Counter(v3).most_common()[0][1]
    v10 = len(v6) - Counter(v6).most_common()[0][1]
    print(v9 + v10)
elif len(v7) == 1 and len(v8) == 1:
    print(len(v3))
else:
    v11 = len(v3) - Counter(v3).most_common()[0][1] + len(v6) - Counter(v6).most_common()[1][1]
    v12 = len(v3) - Counter(v3).most_common()[1][1] + len(v6) - Counter(v6).most_common()[0][1]
    print(min(v11, v12))
