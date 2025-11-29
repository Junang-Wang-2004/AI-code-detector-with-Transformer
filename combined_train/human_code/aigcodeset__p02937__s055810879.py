import bisect
v1 = input()
v2 = input()
v3 = set(list(v1))
for v4 in v2:
    if not v4 in v3:
        print(-1)
        exit()
v5 = [[] for v6 in range(26)]
for v7, v8 in enumerate(v1):
    v5[ord(v8) - ord('a')].append(v7)
v9 = 0
v10 = 0
for v7, v4 in enumerate(v2):
    v11 = bisect.bisect_left(v5[ord(v4) - ord('a')], v10)
    if v11 < len(v5[ord(v4) - ord('a')]):
        v11 = v5[ord(v4) - ord('a')][v11]
        v9 += v11 - v10 + 1
        v10 = (v11 + 1) % len(v1)
    else:
        v9 += len(v1) - v10
        v10 = 0
        v11 = bisect.bisect_left(v5[ord(v4) - ord('a')], 0)
        v11 = v5[ord(v4) - ord('a')][v11]
        v9 += v11 - v10 + 1
        v10 = v11 + 1
print(v9)
