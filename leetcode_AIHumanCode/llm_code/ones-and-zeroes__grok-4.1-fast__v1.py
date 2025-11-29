class Solution:
    def findMaxForm(self, strs, m, n):
        items = []
        for s in strs:
            z = s.count('0')
            o = s.count('1')
            items.append((z, o))
        
        table = [[0] * (n + 1) for _ in range(m + 1)]
        
        for z, o in items:
            for x in range(m, z - 1, -1):
                for y in range(n, o - 1, -1):
                    table[x][y] = max(table[x][y], table[x - z][y - o] + 1)
        
        return table[m][n]
