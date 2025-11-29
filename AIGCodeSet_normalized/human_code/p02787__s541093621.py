import bisect
v1, v2 = map(int, list(input().split()))
v3 = []
v4 = 0
for v5 in range(v2):
    v3.append(list(map(int, list(input().split()))))
    v4 = max(v4, v3[-1][0])
v6 = [int(1000000000.0)] * int(1000000.0)
v7 = [False] * int(1000000.0)
v6[0] = 0
v8 = [0]
while len(v8) > 0:
    v9 = v8.pop(0)
    if v9 > v1:
        break
    for v10 in range(v2):
        if v7[v9 + v3[v10][0]] == False:
            bisect.insort_right(v8, v9 + v3[v10][0])
            v7[v9 + v3[v10][0]] = True
        v6[v9 + v3[v10][0]] = min(v6[v9 + v3[v10][0]], v6[v9] + v3[v10][1])
print(min(v6[v9 - 1:]))
