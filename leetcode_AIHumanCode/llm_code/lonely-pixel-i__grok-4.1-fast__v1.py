class Solution(object):
    def findLonelyPixel(self, picture):
        m, n = len(picture), len(picture[0])
        row_counts = [r.count('B') for r in picture]
        col_counts = [sum(r[j] == 'B' for r in picture) for j in range(n)]
        return sum(picture[i][j] == 'B' and row_counts[i] == 1 and col_counts[j] == 1
                   for i in range(m) for j in range(n))
