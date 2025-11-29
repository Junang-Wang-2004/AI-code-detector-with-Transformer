# Time:  O(n^2)
# Space: O(1)
# brute force
class Solution2(object):
    def countCompleteDayPairs(self, hours):
        """
        """
        return sum((hours[i]+hours[j])%24 == 0 for i in range(len(hours)-1) for j in range(i+1, len(hours)))
