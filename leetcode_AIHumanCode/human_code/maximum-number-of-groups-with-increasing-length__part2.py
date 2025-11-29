# Time:  O(nlogn)
# Space: O(1)
# constructive algorithms, sort, greedy
class Solution2(object):
    def maxIncreasingGroups(self, usageLimits):
        """
        """
        usageLimits.sort()
        result = curr = 0
        for x in usageLimits:
            curr += x
            if curr >= result+1:
                curr -= result+1
                result += 1
        return result

    
