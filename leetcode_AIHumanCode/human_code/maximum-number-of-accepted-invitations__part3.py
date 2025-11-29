# Time:  O(|V| * |E|) = O(min(m, n) * (m * n))
# Space: O(|V|) = O(min(m, n))
# Hungarian bipartite matching with less space
class Solution2(object):
    def maximumInvitations(self, grid):
        """
        """
        def augment(grid, u, lookup, match):
            for v in range(V):
                if not get_grid(u, v) or v in lookup:
                    continue
                lookup.add(v)
                if v not in match or augment(grid, match[v], lookup, match):
                    match[v] = u  # greedily match
                    return True
            return False
    
        def hungarian(grid):
            match = {}
            for i in range(U):
                augment(grid, i, set(), match)
            return len(match)

        U, V = min(len(grid), len(grid[0])), max(len(grid), len(grid[0]))
        get_grid = (lambda x, y: grid[x][y]) if len(grid) < len(grid[0]) else (lambda x, y: grid[y][x])
        return hungarian(grid)


