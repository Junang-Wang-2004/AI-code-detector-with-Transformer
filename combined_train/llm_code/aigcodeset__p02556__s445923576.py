v1 = int(input())
v2 = [0, 10 ** 9]
v3 = [0, 0]
v4 = [10 ** 9, 10 ** 9]
v5 = [10 ** 9, 0]
for v6 in range(0, v1):
    v7, v8 = list(map(int, input().split()))
    if v3[0] < v7 and v3[1] < v8:
        v3 = [v7, v8]
    if v2[0] < v7 and v2[1] > v8:
        v2 = [v7, v8]
    if v5[0] > v7 and v5[1] < v8:
        v5 = [v7, v8]
    if v4[0] > v7 and v4[1] > v8:
        v4 = [v7, v8]
v9 = abs(v3[0] - v4[0]) + abs(v3[1] - v4[1])
v10 = abs(v5[0] - v2[0]) + abs(v5[1] - v4[1])
v11 = abs(v3[0] - v3[1]) + abs(v2[0] - v4[1])
v12 = abs(v5[0] - v5[1]) + abs(v2[0] - v4[1])
print(max(v9, v10, v11, v12))
