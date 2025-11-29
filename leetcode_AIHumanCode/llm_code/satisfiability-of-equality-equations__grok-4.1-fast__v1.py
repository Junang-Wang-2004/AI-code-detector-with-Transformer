class Solution:
    def equationsPossible(self, equations):
        adj = [[False] * 26 for _ in range(26)]
        for expr in equations:
            u = ord(expr[0]) - ord('a')
            v = ord(expr[3]) - ord('a')
            if expr[1] == '!':
                if u == v:
                    return False
            else:
                adj[u][v] = True
                adj[v][u] = True
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if adj[i][k] and adj[k][j]:
                        adj[i][j] = True
        for expr in equations:
            if expr[1] == '!':
                u = ord(expr[0]) - ord('a')
                v = ord(expr[3]) - ord('a')
                if adj[u][v]:
                    return False
        return True
