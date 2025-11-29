import numpy as np
v1 = input().split(' ')
v2 = int(v1[0])
v3 = int(v1[1])
v4 = int(v1[2])
v5 = []
v6 = []
v7 = []
v8 = [0] * v3
v9 = 0
for v10 in range(v2):
    v11 = input().split(' ')
    v12 = int(v11[0])
    v6.append(v12)
    v5.append([int(v11[v10]) for v10 in range(1, v3 + 1)])
    v7.append([v12 / int(v11[v10]) if int(v11[v10]) != 0 else float('inf') for v10 in range(1, v3 + 1)])
v5 = np.array(v5)
while len(v7) > 0:
    v13 = np.argmin(v7, axis=0)
    v14 = np.min(v7, axis=0)
    v15 = np.argmax(v14)
    v8 = [v8[j] + v5[v15][j] for v16 in range(v3)]
    v9 += v6[v15]
    if all((v >= v4 for v17 in v8)):
        print(v9)
        break
    v7 = np.delete(v7, v15, 0)
    v5 = np.delete(v5, v15, 0)
    v6.pop(v15)
else:
    print(-1)
