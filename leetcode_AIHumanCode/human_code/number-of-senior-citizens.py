# Time:  O(n)
# Space: O(1)

# string
class Solution(object):
    def countSeniors(self, details):
        """
        """
        return sum(x[-4:-2] > "60" for x in details)
