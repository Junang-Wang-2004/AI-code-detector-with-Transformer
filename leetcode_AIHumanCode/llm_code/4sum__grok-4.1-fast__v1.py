class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        n = len(nums)
        for p in range(n - 3):
            if p > 0 and nums[p] == nums[p - 1]:
                continue
            for q in range(p + 1, n - 2):
                if q > p + 1 and nums[q] == nums[q - 1]:
                    continue
                remain = target - nums[p] - nums[q]
                start = q + 1
                end = n - 1
                while start < end:
                    curr_sum = nums[start] + nums[end]
                    if curr_sum == remain:
                        ans.append([nums[p], nums[q], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                    elif curr_sum < remain:
                        start += 1
                    else:
                        end -= 1
        return ans
