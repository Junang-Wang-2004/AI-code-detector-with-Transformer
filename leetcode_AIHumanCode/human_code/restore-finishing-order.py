# Time:  O(n + min(8, n))
# Space: O(min(8, n))

# hash table
class Solution(object):
    def recoverOrder(self, order, friends):
        """
        """
        lookup = set(friends)
        return [x for x in order if x in lookup]
