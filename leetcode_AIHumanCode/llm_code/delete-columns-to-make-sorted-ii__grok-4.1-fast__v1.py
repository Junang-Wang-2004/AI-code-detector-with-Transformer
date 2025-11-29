class Solution:
    def minDeletionSize(self, strs):
        if not strs or len(strs) < 2:
            return 0
        n = len(strs)
        m = len(strs[0])
        pending = [True] * (n - 1)
        count = 0
        for j in range(m):
            needs_delete = any(pending[i] and strs[i][j] > strs[i + 1][j] for i in range(n - 1))
            if needs_delete:
                count += 1
                continue
            for i in range(n - 1):
                if pending[i] and strs[i][j] < strs[i + 1][j]:
                    pending[i] = False
        return count
