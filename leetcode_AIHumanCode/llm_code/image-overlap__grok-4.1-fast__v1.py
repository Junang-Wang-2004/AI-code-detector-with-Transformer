class Solution:
    def largestOverlap(self, A, B):
        n = len(A)
        result = 0
        for shx in range(1 - n, n):
            for shy in range(1 - n, n):
                matches = 0
                for x in range(n):
                    yb = x - shx
                    if not 0 <= yb < n:
                        continue
                    for y in range(n):
                        xb = y - shy
                        if 0 <= xb < n and A[x][y] and B[yb][xb]:
                            matches += 1
                result = max(result, matches)
        return result
