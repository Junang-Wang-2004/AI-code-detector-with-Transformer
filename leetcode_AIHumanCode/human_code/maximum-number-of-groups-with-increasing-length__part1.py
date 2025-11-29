# Time:  O(n)
# Space: O(n)

# constructive algorithms, counting sort, greedy
class Solution(object):
    def maxIncreasingGroups(self, usageLimits):
        """
        """
        def inplace_counting_sort(nums, reverse=False):  # Time: O(n)
            if not nums:
                return
            count = [0]*(max(nums)+1)
            for num in nums:
                count[num] += 1
            for i in range(1, len(count)):
                count[i] += count[i-1]
            for i in reversed(range(len(nums))):  # inplace but unstable sort
                while nums[i] >= 0:
                    count[nums[i]] -= 1
                    j = count[nums[i]]
                    nums[i], nums[j] = nums[j], ~nums[i]
            for i in range(len(nums)):
                nums[i] = ~nums[i]  # restore values
            if reverse:  # unstable sort
                nums.reverse()

        usageLimits = [min(x, len(usageLimits)) for x in usageLimits]
        inplace_counting_sort(usageLimits)
        result = curr = 0
        for x in usageLimits:
            curr += x
            if curr >= result+1:
                curr -= result+1
                result += 1
        return result


