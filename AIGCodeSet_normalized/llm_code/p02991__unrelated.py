from collections import deque

def f1(a1, a2, a3):
    v1 = deque([(a2, 0, 0)])
    v2 = set([a2])
    while v1:
        v3, v4, v5 = v1.popleft()
        if v3 == a3 and v4 % 3 == 0:
            return v5
        for v6 in a1[v3]:
            if v6 not in v2:
                v2.add(v6)
                v1.append((v6, v4 + 1, v5 + (v4 + 1) // 3))
    return -1

def f2(a1, a2, a3, a4, a5):
    v1 = [[] for v2 in range(a1 + 1)]
    for v3, v4 in a3:
        v1[v3].append(v4)
    return f1(v1, a4, a5)
v1, v2 = map(int, input().split())
v3 = [tuple(map(int, input().split())) for v4 in range(v2)]
v5, v6 = map(int, input().split())
print(f2(v1, v2, v3, v5, v6))
