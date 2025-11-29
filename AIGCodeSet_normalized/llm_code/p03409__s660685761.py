import bisect
v1 = -1
v2 = int(input())
v3 = [v1] * 101
v4 = [v1] * 101
for v5 in range(v2):
    v6 = list(map(int, input().split()))
    v3[v6[0]] = v6[1]
for v5 in range(v2):
    v6 = list(map(int, input().split()))
    v4[v6[0]] = v6[1]
v7 = 0
for v5 in range(101):
    if v3[v5] != v1:
        v8 = bisect.bisect_left(v4, v3[v5], v5 + 1)
        if v8 < len(v4) and v4[v8] > v3[v5]:
            v7 += 1
            v3[v5] = v1
            v4[v8] = v1
print(v7)
