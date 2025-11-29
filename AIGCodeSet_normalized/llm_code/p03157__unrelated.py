import sys

def f1(a1, a2, a3, a4):
    if a1 < 0 or a1 >= h or a2 < 0 or (a2 >= w) or (grid[a1][a2] != a3):
        return
    if a4 % 2 == 1 and grid[a1][a2] == '.':
        count[0] += 1
    grid[a1][a2] = '!'
    for v1, v2 in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        f1(a1 + v1, a2 + v2, '.' if a3 == '#' else '#', a4 + 1)
v1, v2 = map(int, sys.stdin.readline().split())
v3 = [list(sys.stdin.readline().strip()) for v4 in range(v1)]
v5 = [0]
for v6 in range(v1):
    for v7 in range(v2):
        if v3[v6][v7] == '#':
            f1(v6, v7, '#', 1)
print(v5[0])
