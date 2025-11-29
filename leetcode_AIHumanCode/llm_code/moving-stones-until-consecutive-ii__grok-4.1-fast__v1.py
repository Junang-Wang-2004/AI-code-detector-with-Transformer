class Solution(object):
    def numMovesStonesII(self, nums):
        nums.sort()
        length = len(nums)
        option1 = nums[-1] - nums[1] - length + 2
        option2 = nums[-2] - nums[0] - length + 2
        maxm = max(option1, option2)
        minm = length
        r = 0
        for l in range(length):
            while r < length and nums[r] - nums[l] + 1 <= length:
                r += 1
            cnt = r - l
            if cnt == 0:
                continue
            wsp = nums[r - 1] - nums[l] + 1
            outs = length - cnt
            if outs == 1 and wsp == length - 1:
                minm = min(minm, 2)
            else:
                minm = min(minm, outs)
        return [minm, maxm]
