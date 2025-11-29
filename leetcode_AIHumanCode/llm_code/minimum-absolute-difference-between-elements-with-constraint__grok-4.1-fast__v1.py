from sortedcontainers import SortedList

class Solution(object):
    def minAbsoluteDifference(self, nums, x):
        s_list = SortedList()
        minimum = float("inf")
        prefix_end = 0
        for curr in range(len(nums)):
            while prefix_end <= curr - x:
                s_list.add(nums[prefix_end])
                prefix_end += 1
            if curr >= x:
                ins_pos = s_list.bisect_left(nums[curr])
                prev_diff = nums[curr] - s_list[ins_pos - 1] if ins_pos > 0 else float("inf")
                next_diff = s_list[ins_pos] - nums[curr] if ins_pos < len(s_list) else float("inf")
                minimum = min(minimum, prev_diff, next_diff)
        return minimum
