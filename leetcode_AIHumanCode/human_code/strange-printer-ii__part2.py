# Time:  O(c * m * n + e), c is the number of colors
#                        , e is the number of edges in adj, at most O(c^2)
# Space: O(e)
class Solution2(object):
    def isPrintable(self, targetGrid):
        """
        """
        VISITING, VISITED = list(range(2))
        def has_cycle(adj, color, lookup):
            lookup[color] = VISITING
            for new_color in adj[color]:
                if (new_color not in lookup and has_cycle(adj, new_color, lookup)) or \
                   lookup[new_color] == VISITING:
                    return True
            lookup[color] = VISITED
            return False          

        MAX_COLOR = 60
        adj = collections.defaultdict(set)
        for color in range(1, MAX_COLOR+1):
            min_r = len(targetGrid)
            min_c = len(targetGrid[0])
            max_r = -1
            max_c = -1
            for r in range(len(targetGrid)):
                for c in range(len(targetGrid[r])):
                    if targetGrid[r][c] == color:
                        min_r = min(min_r, r)
                        min_c = min(min_c, c)
                        max_r = max(max_r, r)
                        max_c = max(max_c, c)
            for r in range(min_r, max_r+1):
                for c in range(min_c, max_c+1):
                    if targetGrid[r][c] != color:
                        adj[color].add(targetGrid[r][c])

        lookup = {}
        return all(color in lookup or not has_cycle(adj, color, lookup) for color in range(1, MAX_COLOR+1))
