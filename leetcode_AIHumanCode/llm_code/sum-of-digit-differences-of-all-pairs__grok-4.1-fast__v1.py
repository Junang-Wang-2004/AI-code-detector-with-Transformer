class Solution:
    def sumDigitDifferences(self, nums):
        n = len(nums)
        L = max(len(str(num)) for num in nums)
        pos_counts = [[0] * 10 for _ in range(L)]
        for num in nums:
            s = str(num).zfill(L)
            for i, ch in enumerate(s):
                pos_counts[i][int(ch)] += 1
        result = 0
        for counts in pos_counts:
            sq_sum = sum(c * c for c in counts)
            result += (n * n - sq_sum) // 2
        return result
