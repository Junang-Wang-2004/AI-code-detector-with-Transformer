# Time:  O(s + logn), s is the number of elements in the array
# Space: O(1)

class Solution(object):
    def minPatches(self, nums, n):
        """
        """
        result = reachable = 0
        for x in nums:
            if x > n:
                break
            while not reachable >= x-1:
                result += 1
                reachable += reachable+1
            reachable += x
        while not reachable >= n:
            result += 1
            reachable += reachable+1
        return result


