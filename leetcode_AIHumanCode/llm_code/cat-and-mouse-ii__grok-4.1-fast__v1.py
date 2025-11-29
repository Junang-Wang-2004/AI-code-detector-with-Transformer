from collections import deque

class Solution:
    def canMouseWin(self, grid, catJump, mouseJump):
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        N = rows * cols
        wall = [False] * N
        food, mstart, cstart = -1, -1, -1
        for r in range(rows):
            for c in range(cols):
                i = r * cols + c
                ch = grid[r][c]
                if ch == '#':
                    wall[i] = True
                elif ch == 'F':
                    food = i
                elif ch == 'M':
                    mstart = i
                elif ch == 'C':
                    cstart = i
        mmoves = [set() for _ in range(N)]
        cmoves = [set() for _ in range(N)]
        for r in range(rows):
            for c in range(cols):
                i = r * cols + c
                if wall[i]: continue
                mmoves[i].add(i)
                cmoves[i].add(i)
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    k = 1
                    while k <= mouseJump and 0 <= nr < rows and 0 <= nc < cols and not wall[nr * cols + nc]:
                        mmoves[i].add(nr * cols + nc)
                        nr += dr
                        nc += dc
                        k += 1
                    nr, nc = r + dr, c + dc
                    k = 1
                    while k <= catJump and 0 <= nr < rows and 0 <= nc < cols and not wall[nr * cols + nc]:
                        cmoves[i].add(nr * cols + nc)
                        nr += dr
                        nc += dc
                        k += 1
        TM, TC = 0, 1
        WM, WC = 1, 2
        col = [[[0] * 2 for _ in range(N)] for _ in range(N)]
        deg = [[len(cmoves[j]) for j in range(N)] for _ in range(N)]
        qu = deque()
        for j in range(N):
            if wall[j] or j == food: continue
            col[food][j][TC] = WM
            qu.append((food, j, TC))
            col[j][food][TM] = WC
        for j in range(N):
            if wall[j] or j == food: continue
            col[j][j][TM] = WC
            col[j][j][TC] = WC
        while qu:
            mx, cx, turn = qu.popleft()
            if turn == TC:
                for pm in mmoves[mx]:
                    pt = TM
                    pc = cx
                    if col[pm][pc][pt]: continue
                    col[pm][pc][pt] = WM
                    qu.append((pm, pc, pt))
            else:
                for pc in cmoves[cx]:
                    pt = TC
                    pm = mx
                    if col[pm][pc][pt]: continue
                    deg[pm][pc] -= 1
                    if deg[pm][pc] == 0:
                        col[pm][pc][pt] = WM
                        qu.append((pm, pc, pt))
        return col[mstart][cstart][TM] == WM
