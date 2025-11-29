from collections import deque
v1 = int(input())
v2 = [[] for v3 in range(v1)]
for v3 in range(v1 - 1):
    v4, v5 = map(int, input().split())
    v4 = v4 - 1
    v5 = v5 - 1
    v2[v4].append(v5)
    v2[v5].append(v4)
v6 = [0] * v1
v6[0] = 1
v7 = [0] * v1
v7[0] = -1
v8 = [1] * v1
v9 = deque([0])
v10 = deque([0])
v11 = [[] for v3 in range(v1)]
while len(v9) > 0:
    v12 = v9[0]
    v9.popleft()
    for v3 in range(len(v2[v12])):
        if v6[v2[v12][v3]] == 0:
            v6[v2[v12][v3]] = 1
            v9.append(v2[v12][v3])
            v10.append(v2[v12][v3])
            v7[v2[v12][v3]] = v12
v10 = list(v10)[::-1]
for v3 in range(v1):
    if v10[v3] != 0:
        v8[v7[v10[v3]]] += v8[v10[v3]]
v4 = 0
v3 = v1 - 1
while v3 != 0:
    v3 = v7[v3]
    v4 = v4 + 1
v3 = v1 - 1
for v13 in range((v4 - 1) // 2):
    v3 = v7[v3]
v14 = v8[v3]
v15 = v1 - v8[v3]
if v15 > v14:
    print('Fennec')
else:
    print('Snuke')
