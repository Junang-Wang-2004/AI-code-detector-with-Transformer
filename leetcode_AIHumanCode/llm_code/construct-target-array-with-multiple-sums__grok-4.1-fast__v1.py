class Solution(object):
    def isPossible(self, target):
        n = len(target)
        cursum = sum(target)
        nums = sorted(target, reverse=True)
        while cursum > n:
            y = nums[0]
            rem = cursum - y
            if rem <= 0:
                return False
            x = 2 * y - cursum
            if x <= 0:
                return False
            if x > rem:
                x = x % rem + rem
            nums[0] = x
            cursum = x + rem
            nums.sort(reverse=True)
        return cursum == n
