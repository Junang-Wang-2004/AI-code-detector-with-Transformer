from _collections import deque
v1, v2, v3 = map(int, input().split())
v4 = [input() for v5 in range(v1)]
v6 = deque([])
v7 = 1

def f1(a1):
    global cnt
    v1 = []
    v2 = a1.count('#')
    v3 = 0
    for v4 in a1:
        v1.append(v7)
        if v4 == '#':
            v5 += 1
            v3 += 1
            if v3 == v2:
                for v6 in range(v2 - len(v1)):
                    v1.append(v5 - 1)
                break
    v6.append(v1)
for v8 in range(v1):
    if v4[v8].count('#') == 0 and v8 != 0 and (len(v6) != 0):
        v6.append(v6[-1])
    elif v4[v8].count('#') != 0:
        f1(v4[v8])
if len(v6) != v1:
    for v5 in range(v1 - len(v6)):
        v6.appendleft(v6[0])
for v9 in v6:
    print(*v9)
