from collections import deque

class Solution(object):
    def minPushBox(self, grid):
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def player_can_reach(fr, fc, tr, tc, br, bc):
            if fr == tr and fc == tc:
                return True
            stack = [(fr, fc)]
            seen = set([(fr, fc)])
            while stack:
                r, c = stack.pop()
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    pos = (nr, nc)
                    if (0 <= nr < m and 0 <= nc < n and
                        grid[nr][nc] != '#' and
                        pos != (br, bc) and
                        pos not in seen):
                        if nr == tr and nc == tc:
                            return True
                        seen.add(pos)
                        stack.append(pos)
            return False
        
        boxr = boxc = playr = playc = tr = tc = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B':
                    boxr, boxc = i, j
                elif grid[i][j] == 'S':
                    playr, playc = i, j
                elif grid[i][j] == 'T':
                    tr, tc = i, j
        
        q = deque([(boxr, boxc, playr, playc, 0)])
        visited = set([(boxr, boxc, playr, playc)])
        
        while q:
            br, bc, pr, pc, pushes = q.popleft()
            if br == tr and bc == tc:
                return pushes
            for dr, dc in dirs:
                nbr = br + dr
                nbc = bc + dc
                if not (0 <= nbr < m and 0 <= nbc < n and grid[nbr][nbc] != '#'):
                    continue
                pfr = br - dr
                pfc = bc - dc
                if not (0 <= pfr < m and 0 <= pfc < n and grid[pfr][pfc] != '#'):
                    continue
                if player_can_reach(pr, pc, pfr, pfc, br, bc):
                    npr = br
                    npc = bc
                    state = (nbr, nbc, npr, npc)
                    if state not in visited:
                        visited.add(state)
                        q.append((nbr, nbc, npr, npc, pushes + 1))
        return -1
