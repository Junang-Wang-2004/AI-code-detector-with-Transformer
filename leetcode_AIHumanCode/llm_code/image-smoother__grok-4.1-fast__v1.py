class Solution:
    def imageSmoother(self, M):
        if not M or not M[0]:
            return []
        h, w = len(M), len(M[0])
        res = [[0] * w for _ in range(h)]
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (0, 0)]
        for i in range(h):
            for j in range(w):
                sm = 0
                ct = 0
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < h and 0 <= nj < w:
                        sm += M[ni][nj]
                        ct += 1
                res[i][j] = sm // ct
        return res
