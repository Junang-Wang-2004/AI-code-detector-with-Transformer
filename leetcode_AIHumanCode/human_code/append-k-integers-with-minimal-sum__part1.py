# Time:  O(nlogn)
# Space: O(n)

# greedy
class Solution(object):
    def minimalKSum(self, nums, k):
        """
        """
        result = k*(k+1)//2
        curr = k+1
        for x in sorted(set(nums)):
            if x < curr:
                result += curr-x
                curr += 1
        return result


