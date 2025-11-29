from collections import deque

class Solution:
    def minFlips(self, mat):
        if not mat or not mat[0]:
            return 0
        rows = len(mat)
        cols = len(mat[0])
        total = rows * cols
        
        def cell(r, c):
            return r * cols + c
        
        init = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]:
                    init |= (1 << cell(i, j))
        
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]
        masks = [0] * total
        for sr in range(rows):
            for sc in range(cols):
                idx = cell(sr, sc)
                cmask = 0
                for dr, dc in deltas:
                    nr = sr + dr
                    nc = sc + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        cmask |= (1 << cell(nr, nc))
                masks[idx] = cmask
        
        q = deque([(init, 0)])
        seen = {init}
        while q:
            curr, steps = q.popleft()
            if curr == 0:
                return steps
            for msk in masks:
                nxt = curr ^ msk
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, steps + 1))
        return -1
