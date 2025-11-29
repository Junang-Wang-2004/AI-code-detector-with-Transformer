from collections import Counter
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = Counter(v2)
v3 = sorted(v3.items())
v4 = []
for v5, v6 in v3:
    v4.append([v5, v6])
v3 = v4
v7 = len(v3)
v8 = 0
v9 = v7 - 1
while True:
    if v3[v8][1] < 2:
        for v8 in range(v7):
            if v3[v8][1] > 1:
                break
    if v3[v9][1] < 2:
        for v9 in range(v7):
            if v3[v7 - v9 - 1][1] > 1:
                break
        v9 = v7 - v9 - 1
    if v3[v8][1] <= 1 and v3[v9][1] <= 1:
        break
    if v8 == v9:
        if v3[v8][1] >= 3:
            v3[v8][1] -= 2
        else:
            v3[v8][1] -= 1
            for v10 in range(v8 + 1, v7):
                if v3[v10][1] > 0:
                    v3[v10][1] -= 1
                    break
    else:
        v3[v8][1] -= 1
        v3[v9][1] -= 1
v11 = 0
for v5, v6 in v3:
    v11 += v6
print(v11)
