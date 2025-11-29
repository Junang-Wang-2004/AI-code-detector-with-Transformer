import bisect
v1 = int(input())
v2 = list(map(int, input().split()))
v2 = sorted(v2)
if v1 == 2:
    print(max(v2), min(v2))
    exit()
v3 = v2[v1 - 1]
v4 = v3 // 2
v5 = bisect.bisect_left(v2, v4)
if abs(v4 - v2[v5 - 1]) < abs(v4 - v2[v5]) and abs(v4 - v2[v5 - 1]) < abs(v4 - v2[v5 + 1]):
    v6 = v2[v5 - 1]
elif abs(v4 - v2[v5]) < abs(v4 - v2[v5 + 1]):
    v6 = v2[v5]
else:
    v6 = v2[v5 + 1]
print(v3, v6)
