from collections import deque

def f1(a1):
    v1 = deque([a1])
    v2, v3 = (0, 0)
    while len(v1) > 0:
        v4, v5 = v1.popleft()
        v2 += int(s[v4][v5] == '#')
        v3 += int(s[v4][v5] == '.')
        for v6, v7 in near[v4][v5]:
            if (v6, v7) in frag:
                continue
            if s[v6][v7] != s[v4][v5]:
                (v1.append((v6, v7)), frag.add((v6, v7)))
    return v2 * v3
v1, v2 = map(int, input().split())
v3 = [input() for v4 in range(v1)]
v5 = [[set() for v6 in range(v2)] for v7 in range(v1)]
for v7, v8 in enumerate(v3):
    for v6, v9 in enumerate(v8):
        for v10, v11 in [(v7 - 1, v6), (v7, v6 - 1), (v7 + 1, v6), (v7, v6 + 1)]:
            if 0 <= v10 < v1 and 0 <= v11 < v2 and (v3[v10][v11] != v9):
                v5[v7][v6].add((v10, v11))
v12, v13 = (0, set())
for v7 in range(v1):
    for v6 in range(v2):
        if (v7, v6) not in v13:
            v13.add((v7, v6))
            v12 += f1((v7, v6))
print(v12)
