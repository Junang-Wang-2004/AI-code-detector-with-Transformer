# Time:  O(n^2)
# Space: O(1)

# dp
class Solution(object):
    def findCoins(self, numWays):
        """
        """
        result = []
        for i in range(1, len(numWays)+1):
            if numWays[i-1] == 1:
                result.append(i)
                for j in reversed(range(i, len(numWays)+1)):
                    numWays[j-1] -= numWays[(j-i)-1] if (j-i)-1 >= 0 else 1
            if numWays[i-1]:
                return []
        return result


