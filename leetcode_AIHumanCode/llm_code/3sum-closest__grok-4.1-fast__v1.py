class Solution:
    def threeSumClosest(self, nums, target):
        sorted_nums = sorted(nums)
        closest = 0
        smallest_diff = float('inf')
        n = len(sorted_nums)
        for k in range(n - 2):
            if k > 0 and sorted_nums[k] == sorted_nums[k - 1]:
                continue
            j = k + 1
            m = n - 1
            while j < m:
                curr_sum = sorted_nums[k] + sorted_nums[j] + sorted_nums[m]
                if curr_sum == target:
                    return target
                diff = abs(curr_sum - target)
                if diff < smallest_diff:
                    smallest_diff = diff
                    closest = curr_sum
                if curr_sum < target:
                    j += 1
                else:
                    m -= 1
        return closest
