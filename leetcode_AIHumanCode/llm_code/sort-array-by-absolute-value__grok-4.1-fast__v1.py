class Solution:
    def sortByAbsoluteValue(self, nums):
        max_val = 0
        for num in nums:
            max_val = max(max_val, abs(num))
        buckets = [[] for _ in range(max_val + 1)]
        for num in nums:
            buckets[abs(num)].append(num)
        ans = []
        for bucket in buckets:
            ans.extend(bucket)
        return ans
