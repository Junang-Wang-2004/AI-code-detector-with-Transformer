class Solution(object):
    def secondGreaterElement(self, nums):
        ans = [-1] * len(nums)
        need_first = []
        need_second = []
        for i in range(len(nums)):
            num = nums[i]
            while need_second and nums[need_second[-1]] < num:
                ans[need_second.pop()] = num
            transfer = []
            while need_first and nums[need_first[-1]] < num:
                transfer.append(need_first.pop())
            need_first.append(i)
            while transfer:
                need_second.append(transfer.pop())
        return ans
