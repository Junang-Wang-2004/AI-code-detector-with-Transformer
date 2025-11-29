class Solution:
    def makeArrayPositive(self, nums):
        cnt = 0
        INF = 10**18 + 42
        last_but_one = nums[0]
        last = last_but_one + nums[1]
        max_old = 0
        for j in range(2, len(nums)):
            candidate = last + nums[j]
            if candidate <= max_old:
                candidate = last + INF
                cnt += 1
            max_old = max(max_old, last_but_one)
            last_but_one = last
            last = candidate
        return cnt
