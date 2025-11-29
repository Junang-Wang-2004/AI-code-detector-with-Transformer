# Time:  O(s + logn), s is the number of elements in the array
# Space: O(1)
class Solution2(object):
    def minPatches(self, nums, n):
        """
        """
        result = reachable = 0
        for x in nums:
            while not reachable >= x-1:
                result += 1
                reachable += reachable+1
                if reachable >= n:
                    return result
            reachable += x
            if reachable >= n:
                return result
        while not reachable >= n:
            result += 1
            reachable += reachable+1
        return result


