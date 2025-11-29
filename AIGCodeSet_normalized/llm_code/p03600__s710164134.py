import heapq
v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v4 = [[] for v3 in range(v1)]
v5 = []
v6 = 0
for v7 in range(v1):
    for v8 in range(v7 + 1, v1):
        v5.append((v2[v7][v8], (v7, v8)))
v5.sort()
v9 = [[-1] * v1 for v3 in range(v1)]

def f1(a1, a2):
    global dd
    v1 = []
    v2 = v9[a2]
    v2[a2] = 0
    heapq.heappush(v1, (0, a2))
    while v1:
        v3, v4 = heapq.heappop(v1)
        for v5, v6 in a1[v4]:
            if v2[v5] == -1 or v2[v5] > v3 + v6:
                v2[v5] = v3 + v6
                heapq.heappush(v1, (v3 + v6, v5))
    return v2
for v10, v11 in v5:
    v12 = f1(v4, v11[0])
    if v12[v11[1]] == -1:
        v4[v11[0]].append((v11[1], v10))
        v4[v11[1]].append((v11[0], v10))
        v6 += v10
    elif v12[v11[1]] < v10:
        print(-1)
        exit()
    elif v12[v11[1]] > v10:
        v4[v11[0]].append((v11[1], v10))
        v4[v11[1]].append((v11[0], v10))
        v6 += v10
print(v6)
