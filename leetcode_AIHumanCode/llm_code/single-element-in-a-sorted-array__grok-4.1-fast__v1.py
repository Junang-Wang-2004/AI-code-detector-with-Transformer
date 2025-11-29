class Solution:
    def singleNonDuplicate(self, nums):
        begin, finish = 0, len(nums) - 1
        while begin < finish:
            center = (begin + finish) // 2
            partner = center ^ 1
            if partner < len(nums) and nums[partner] == nums[center]:
                begin = center + 1
            else:
                finish = center
        return nums[begin]
