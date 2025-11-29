class Solution:
    def findLength(self, nums1, nums2):
        rows = len(nums1)
        cols = len(nums2)
        longest = 0
        matrix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if nums1[r - 1] == nums2[c - 1]:
                    matrix[r][c] = matrix[r - 1][c - 1] + 1
                    longest = max(longest, matrix[r][c])
        return longest
