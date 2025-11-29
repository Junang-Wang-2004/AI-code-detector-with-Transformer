# Time:  O(1)
# Space: O(1)

class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        """
        N -= max(N-1, 0) // 14 * 14  # 14 is got from Solution2
        for i in range(N):
            cells = [0] + [cells[i-1] ^ cells[i+1] ^ 1 for i in range(1, 7)] + [0]
        return cells


