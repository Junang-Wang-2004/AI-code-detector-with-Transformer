class Solution(object):
    def countCombinations(self, pieces, positions):
        dirs = {
            "rook": [(0, 1), (0, -1), (1, 0), (-1, 0)],
            "bishop": [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            "queen": [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        }
        full = (1 << 7) - 1
        n = len(pieces)
        options = [[] for _ in range(n)]
        for i in range(n):
            r, c = positions[i][0] - 1, positions[i][1] - 1
            sq0 = r * 8 + c
            options[i].append({sq0: full})
            for dr, dc in dirs[pieces[i]]:
                cr, cc = r, c
                for d in range(1, 8):
                    cr += dr
                    cc += dc
                    if not (0 <= cr < 8 and 0 <= cc < 8):
                        break
                    path = {}
                    pr, pc = r, c
                    for step in range(1, d):
                        pr += dr
                        pc += dc
                        path[pr * 8 + pc] = 1 << (step - 1)
                    esq = cr * 8 + cc
                    remain = 8 - d
                    emask = ((1 << remain) - 1) << (d - 1)
                    path[esq] = emask
                    options[i].append(path)
        
        occupied = [0] * 64
        
        def search(idx):
            if idx == n:
                return 1
            total = 0
            for opt in options[idx]:
                changes = []
                clash = any(occupied[s] & m for s, m in opt.items())
                if not clash:
                    for s, m in opt.items():
                        occupied[s] |= m
                        changes.append((s, m))
                    total += search(idx + 1)
                    for s, m in changes:
                        occupied[s] ^= m
            return total
        
        return search(0)
