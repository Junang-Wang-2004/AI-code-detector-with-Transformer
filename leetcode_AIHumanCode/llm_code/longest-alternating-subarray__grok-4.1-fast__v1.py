class Solution:
    def alternatingSubarray(self, nums):
        ans = -1
        streak = 0
        expect = 0
        n = len(nums)
        for i in range(1, n):
            d = nums[i] - nums[i - 1]
            if d != 1 and d != -1:
                streak = 0
                continue
            if streak == 0:
                if d == 1:
                    streak = 2
                    expect = -1
            else:
                if d == expect:
                    streak += 1
                    expect = -expect
                else:
                    streak = 0
                    if d == 1:
                        streak = 2
                        expect = -1
            if streak >= 2:
                ans = max(ans, streak)
        return ans
