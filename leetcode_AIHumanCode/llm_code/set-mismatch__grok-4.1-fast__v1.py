class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        expected = n * (n + 1) // 2
        expected_squares = n * (n + 1) * (2 * n + 1) // 6
        actual = sum(nums)
        actual_squares = sum(x * x for x in nums)
        diff = actual - expected
        sq_diff = actual_squares - expected_squares
        total = sq_diff // diff
        duplicate = (total + diff) // 2
        missing = total - duplicate
        return [duplicate, missing]
