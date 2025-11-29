from collections import Counter

class Solution(object):
    def largestInteger(self, nums, k):
        """
        """
        length = len(nums)
        if k == length:
            return max(nums)
        frequencies = Counter(nums)
        if k == 1:
            return max((num for num, occ in frequencies.items() if occ == 1), default=-1)
        answer = -1
        start_val = nums[0]
        end_val = nums[-1]
        if frequencies[start_val] == 1:
            answer = max(answer, start_val)
        if frequencies[end_val] == 1:
            answer = max(answer, end_val)
        return answer
