class Solution:
    def findMatrix(self, nums):
        counts = {}
        for val in nums:
            counts[val] = counts.get(val, 0) + 1
        if not counts:
            return []
        num_rows = max(counts.values())
        board = [[] for _ in range(num_rows)]
        for key, occ in counts.items():
            for slot in range(occ):
                board[slot].append(key)
        return board
