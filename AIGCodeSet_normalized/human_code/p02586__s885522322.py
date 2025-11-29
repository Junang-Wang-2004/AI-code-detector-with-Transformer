import sys
sys.setrecursionlimit(10 ** 9)
v1 = 10 ** 18
v2 = 10 ** 9 + 7
input = lambda: sys.stdin.readline().rstrip()
v3 = lambda b: bool([print('Yes')] if b else print('No'))
v4 = lambda b: bool([print('YES')] if b else print('NO'))
v5 = lambda x: int(x) - 1
v6, v7, v8 = map(int, input().split())
v9 = [[0] * v7 for v10 in range(v6)]
for v11 in range(v8):
    v12, v13, v14 = map(int, input().split())
    v12 -= 1
    v13 -= 1
    v9[v12][v13] = v14
v15 = [[0] * v7 for v10 in range(4)]
for v16 in range(v6):
    for v17 in range(v7):
        for v11 in range(2, -1, -1):
            v15[v11 + 1][v17] = max(v15[v11 + 1][v17], v15[v11][v17] + v9[v16][v17])
        if v17 < v7 - 1:
            for v11 in range(3, -1, -1):
                v15[v11][v17 + 1] = max(v15[v11][v17 + 1], v15[v11][v17])
    if v16 + 1 < v6:
        v18 = 0
        for v17 in range(v7):
            for v11 in range(4):
                v18 = max(v18, v15[v11][v17])
                v15[v11][v17] = 0
            v15[0][v17] = v18
print(max(v15[0][-1], v15[1][-1], v15[2][-1], v15[3][-1]))
