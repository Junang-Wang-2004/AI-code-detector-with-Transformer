class Solution:
    def minOperations(self, nums):
        nums.sort()
        vals = []
        for num in nums:
            if not vals or vals[-1] != num:
                vals.append(num)
        length = len(nums)
        farthest = 0
        start = 0
        for end in range(len(vals)):
            while vals[end] - vals[start] > length - 1:
                start += 1
            farthest = max(farthest, end - start + 1)
        return length - farthest
