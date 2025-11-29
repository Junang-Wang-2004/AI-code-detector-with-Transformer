import collections

class Solution:
    def countCompleteSubarrays(self, nums):
        n = len(nums)
        k = len(set(nums))
        counter = collections.Counter()
        uniques = 0
        total = 0
        end = 0
        for begin in range(n):
            while end < n and uniques < k:
                counter[nums[end]] += 1
                if counter[nums[end]] == 1:
                    uniques += 1
                end += 1
            if uniques == k:
                total += n - end + 1
            counter[nums[begin]] -= 1
            if counter[nums[begin]] == 0:
                uniques -= 1
        return total
