import bisect
v1 = int(input())
v2 = [i * 2 for v3 in list(map(int, input().split()))]
v2.sort()
if v1 == 2:
    print(v2[1] // 2, v2[0] // 2)
    exit()
v4 = v2[-1]
v5 = bisect.bisect_left(v2[:-1], v4 // 2)
v6 = abs(v4 - v2[v5 - 1]) if v5 > 0 else 0
v7 = abs(v4 - v2[v5])
v8 = abs(v4 - v2[v5 + 1]) if v5 < v1 - 2 else 0
if v7 >= v8:
    print(v4 // 2, v2[v5] // 2)
else:
    print(v4 // 2, v2[v5 + 1] // 2)
