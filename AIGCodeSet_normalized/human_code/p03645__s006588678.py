import queue
v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v1)]
for v5 in range(v2):
    v6, v7 = map(lambda n: int(n) - 1, input().split())
    v3[v6].append(v7)
    v3[v7].append(v6)

def f1(a1, a2, a3):
    v1 = queue.Queue()
    v2 = [-1] * a2
    v2[a3] = 0
    v1.put(a3)
    while not v1.empty():
        v3 = v1.get()
        if v2[v3] > 1:
            continue
        for v4 in v3[v3]:
            if v2[v4] != -1:
                continue
            v2[v4] = v2[v3] + 1
            v1.put(v4)
    return v2
if f1(v3, v1, 0)[-1] > 2 or f1(v3, v1, 0)[-1] == -1:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')
