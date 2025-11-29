v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
if v2 == 0:
    print(0)
    exit()
v3 = sorted(v3, key=lambda x: abs(x[0]), reverse=True)
v5 = [[{'S': 0, 'L': [0, 0, 0]} for v6 in range(v1)] for v4 in range(v2 + 1)]
v5[1][0]['L'] = v3[0]
v5[1][0]['S'] = abs(v3[0][0]) + abs(v3[0][1]) + abs(v3[0][2])
for v7 in range(1, v1):
    for v8 in range(1, min(v7 + 2, v2 + 1)):
        v9 = v5[v8 - 1][v7 - 1]['L']
        v9 = [v9[0] + v3[v7][0], v9[1] + v3[v7][1], v9[2] + v3[v7][2]]
        v10 = abs(v9[0]) + abs(v9[1]) + abs(v9[2])
        if v5[v8][v7 - 1]['S'] < v10:
            v5[v8][v7]['S'] = v10
            v5[v8][v7]['L'] = v9
        else:
            v5[v8][v7]['S'] = v5[v8][v7 - 1]['S']
            v5[v8][v7]['L'] = v5[v8][v7 - 1]['L']
v11 = v5[v2][v1 - 1]['S']
v3 = sorted(v3, key=lambda x: abs(x[1]), reverse=True)
v5 = [[{'S': 0, 'L': [0, 0, 0]} for v6 in range(v1)] for v4 in range(v2 + 1)]
v5[1][0]['L'] = v3[0]
v5[1][0]['S'] = abs(v3[0][0]) + abs(v3[0][1]) + abs(v3[0][2])
for v7 in range(1, v1):
    for v8 in range(1, min(v7 + 2, v2 + 1)):
        v9 = v5[v8 - 1][v7 - 1]['L']
        v9 = [v9[0] + v3[v7][0], v9[1] + v3[v7][1], v9[2] + v3[v7][2]]
        v10 = abs(v9[0]) + abs(v9[1]) + abs(v9[2])
        if v5[v8][v7 - 1]['S'] < v10:
            v5[v8][v7]['S'] = v10
            v5[v8][v7]['L'] = v9
        else:
            v5[v8][v7]['S'] = v5[v8][v7 - 1]['S']
            v5[v8][v7]['L'] = v5[v8][v7 - 1]['L']
v11 = max(v5[v2][v1 - 1]['S'], v11)
v3 = sorted(v3, key=lambda x: abs(x[2]), reverse=True)
v5 = [[{'S': 0, 'L': [0, 0, 0]} for v6 in range(v1)] for v4 in range(v2 + 1)]
v5[1][0]['L'] = v3[0]
v5[1][0]['S'] = abs(v3[0][0]) + abs(v3[0][1]) + abs(v3[0][2])
for v7 in range(1, v1):
    for v8 in range(1, min(v7 + 2, v2 + 1)):
        v9 = v5[v8 - 1][v7 - 1]['L']
        v9 = [v9[0] + v3[v7][0], v9[1] + v3[v7][1], v9[2] + v3[v7][2]]
        v10 = abs(v9[0]) + abs(v9[1]) + abs(v9[2])
        if v5[v8][v7 - 1]['S'] < v10:
            v5[v8][v7]['S'] = v10
            v5[v8][v7]['L'] = v9
        else:
            v5[v8][v7]['S'] = v5[v8][v7 - 1]['S']
            v5[v8][v7]['L'] = v5[v8][v7 - 1]['L']
v11 = max(v5[v2][v1 - 1]['S'], v11)
print(v11)
