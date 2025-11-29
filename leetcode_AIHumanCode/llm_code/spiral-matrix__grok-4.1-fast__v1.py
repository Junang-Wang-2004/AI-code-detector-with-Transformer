class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        res = []
        rows, cols = len(matrix), len(matrix[0])
        r_start, r_end = 0, rows - 1
        c_start, c_end = 0, cols - 1
        while r_start <= r_end and c_start <= c_end:
            for c in range(c_start, c_end + 1):
                res.append(matrix[r_start][c])
            r_start += 1
            for r in range(r_start, r_end + 1):
                res.append(matrix[r][c_end])
            c_end -= 1
            if r_start <= r_end:
                for c in range(c_end, c_start - 1, -1):
                    res.append(matrix[r_end][c])
                r_end -= 1
            if c_start <= c_end:
                for r in range(r_end, r_start - 1, -1):
                    res.append(matrix[r][c_start])
                c_start += 1
        return res
