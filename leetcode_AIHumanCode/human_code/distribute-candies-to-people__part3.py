# Time:  O(sqrt(c)), c is the number of candies
# Space: O(1)
class Solution3(object):
    def distributeCandies(self, candies, num_people):
        """
        """
        result = [0]*num_people
        i = 0
        while candies != 0:
            result[i % num_people] += min(candies, i+1)
            candies -= min(candies, i+1)
            i += 1
        return result
