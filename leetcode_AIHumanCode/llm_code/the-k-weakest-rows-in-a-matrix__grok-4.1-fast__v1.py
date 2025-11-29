class Solution:
    def kWeakestRows(self, mat, k):
        candidates = []
        for row_idx, row in enumerate(mat):
            power = 0
            for pos in row:
                if pos == 0:
                    break
                power += 1
            candidates.append((power, row_idx))
        candidates.sort()
        return [row_idx for _, row_idx in candidates[:k]]
