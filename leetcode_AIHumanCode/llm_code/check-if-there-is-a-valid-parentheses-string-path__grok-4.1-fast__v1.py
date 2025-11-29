class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 != 0:
            return False
        prev_bal = [set() for _ in range(n)]
        d = 1 if grid[0][0] == '(' else -1
        if d >= 0:
            prev_bal[0].add(d)
        for j in range(1, n):
            d = 1 if grid[0][j] == '(' else -1
            reachable = set()
            for b in prev_bal[j - 1]:
                nb = b + d
                if nb >= 0:
                    reachable.add(nb)
            prev_bal[j] = reachable
        for i in range(1, m):
            curr_bal = [set() for _ in range(n)]
            d = 1 if grid[i][0] == '(' else -1
            reachable = set()
            for b in prev_bal[0]:
                nb = b + d
                if nb >= 0:
                    reachable.add(nb)
            curr_bal[0] = reachable
            for j in range(1, n):
                d = 1 if grid[i][j] == '(' else -1
                reachable = set()
                for b in curr_bal[j - 1]:
                    nb = b + d
                    if nb >= 0:
                        reachable.add(nb)
                for b in prev_bal[j]:
                    nb = b + d
                    if nb >= 0:
                        reachable.add(nb)
                curr_bal[j] = reachable
            prev_bal = curr_bal
        return 0 in prev_bal[n - 1]
