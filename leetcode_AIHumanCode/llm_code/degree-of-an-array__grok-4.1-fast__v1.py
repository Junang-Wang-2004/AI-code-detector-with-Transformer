class Solution:
    def findShortestSubArray(self, nums):
        count = {}
        start_pos = {}
        end_pos = {}
        for idx in range(len(nums)):
            val = nums[idx]
            count[val] = count.get(val, 0) + 1
            if val not in start_pos:
                start_pos[val] = idx
            end_pos[val] = idx
        max_count = max(count.values())
        result = len(nums) + 1
        for val in count:
            if count[val] == max_count:
                result = min(result, end_pos[val] - start_pos[val] + 1)
        return result
