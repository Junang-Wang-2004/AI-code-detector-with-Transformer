class Solution:
    def countHillValley(self, nums):
        ans = 0
        last_dir = 0
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if diff != 0:
                curr_dir = 1 if diff > 0 else -1
                if last_dir != 0 and curr_dir != last_dir:
                    ans += 1
                last_dir = curr_dir
        return ans
