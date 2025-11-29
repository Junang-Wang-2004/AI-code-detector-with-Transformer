class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        indexed = [(nums[i], i) for i in range(n)]
        indexed.sort()
        ans = [0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and indexed[j + 1][0] - indexed[j][0] <= limit:
                j += 1
            positions = sorted(indexed[k][1] for k in range(i, j + 1))
            for k in range(j - i + 1):
                ans[positions[k]] = indexed[i + k][0]
            i = j + 1
        return ans
