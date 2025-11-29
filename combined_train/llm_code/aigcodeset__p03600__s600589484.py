import heapq
import sys
v1 = int(input())
v2 = []
for v3 in range(v1):
    v4 = list(map(int, input().split()))
    v2.append(v4)
v5 = {}
for v3 in range(v1):
    for v6 in range(v3, v1):
        if v3 != v6:
            v5[v3, v6] = v2[v3][v6]
v5 = sorted(v5.items(), key=lambda x: x[1], reverse=True)

def f1(a1, a2, a3):
    v1 = [float('inf')] * a1
    v1[a2] = 0
    v2 = []
    v3 = [0] * a1
    heapq.heappush(v2, (0, a2))
    while v2:
        v4, v5 = heapq.heappop(v2)
        if v3[v5] == 0:
            v3[v5] = 1
            for v6 in range(a1):
                if a3[v5][v6] != -1:
                    if v1[v6] > v4 + a3[v5][v6]:
                        v1[v6] = v4 + a3[v5][v6]
                        heapq.heappush(v2, (v4 + a3[v5][v6], v6))
    return v1
v7 = [[-1] * v1 for v8 in range(v1)]
v9 = 0
for v3 in range(v1):
    v10, v11 = v5[v3]
    v12, v13 = v10
    v7[v12][v13] = v11
    v7[v13][v12] = v11
    v9 += v11
for v3 in range(v1):
    v14 = f1(v1, v3, v7)
    for v6 in range(v1):
        if v14[v6] != v2[v3][v6]:
            print(-1)
            sys.exit()
for v3 in range(v1):
    v10, v11 = v5[v3]
    v12, v13 = v10
    v7[v12][v13] = -1
    v7[v13][v12] = -1
    v15 = f1(v1, v12, v7)
    v16 = f1(v1, v13, v7)
    v17 = 0
    for v6 in range(v1):
        if v15[v6] != v2[v12][v6] or v16[v6] != v2[v13][v6]:
            v7[v12][v13] = v11
            v7[v13][v12] = v11
            v17 = 1
            break
    if v17 == 0:
        v9 -= v11
print(v9)
