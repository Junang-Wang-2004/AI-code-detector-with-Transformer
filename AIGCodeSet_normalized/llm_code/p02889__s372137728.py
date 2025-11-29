from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix

def f1(a1, a2, a3):
    return f2(a1, a2, a3[a1])

def f2(a1, a2, a3):
    v1 = []
    v2 = a2
    while v2 != a1 and v2 >= 0:
        v1.append(v2)
        v2 = a3[v2]
    if v2 < 0:
        return []
    v1.append(v2)
    return v1[::-1]
v1, v2, v3 = map(int, input().split())
if v2 != 0:
    v4 = [[0 for v5 in range(v1)] for v5 in range(v1)]
    for v6 in range(v2):
        v7, v8, v9 = map(int, input().split())
        v7 -= 1
        v8 -= 1
        if v9 <= v3:
            v4[v7][v8] = v9
            v4[v8][v7] = v9
    v10 = csr_matrix(v4)
    v11, v12 = shortest_path(v10, return_predecessors=True)
v13 = int(input())
for v6 in range(v13):
    if v2 == 0:
        print(-1)
    else:
        v14, v15 = map(int, input().split())
        v14 -= 1
        v15 -= 1
        v16 = f1(v14, v15, v12)
        if len(v16) == 0:
            print(-1)
        else:
            v17 = 0
            v18 = v3
            for v19 in range(len(v16) - 1):
                if v18 - v4[v16[v19]][v16[v19 + 1]] < 0:
                    v17 += 1
                    v18 = v3
                v18 -= v4[v16[v19]][v16[v19 + 1]]
            print(v17)
