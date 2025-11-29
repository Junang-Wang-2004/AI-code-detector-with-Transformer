from collections import defaultdict, deque
v1 = float('inf')
v2, v3 = map(int, input().split())
v4 = defaultdict(list)
v5 = defaultdict(list)
for v6 in range(v3):
    v7, v8 = map(int, input().split())
    v7 -= 1
    v8 -= 1
    v4[v7].append(v8)
    v5[v8].append(v7)
v9 = [-v1] * v2
for v10 in range(v2):
    if v4[v10] == []:
        v9[v10] = 0
        v11 = deque([])
        while v5[v10]:
            v12 = v5[v10].pop()
            v9[v12] = max(v9[v10] + 1, v9[v12])
            v11.append(v12)
        while v11:
            v12 = v11.pop()
            while v5[v12]:
                v13 = v5[v12].pop()
                v9[v13] = max(v9[v12] + 1, v9[v13])
                v11.append(v13)
print(max(v9))
