# Time:  O(4^n)
# Space: O(1)

# array
class Solution(object):
    def specialGrid(self, n):
        """
        """
        def copy(l, r1, c1, r2, c2):
            for i in range(l):
                for j in range(l):
                    result[r2+i][c2+j] = result[r1+i][c1+j]+l*l
        
        total = 1<<n
        result = [[0]*total for _ in range(total)]
        l = 1
        for i in range(n):
            r, c = 0, total-l
            for dr, dc in ((l, 0), (0, -l), (-l, 0)):
                nr, nc = r+dr, c+dc
                copy(l, r, c, nr, nc)
                r, c = nr, nc
            l <<= 1
        return result


