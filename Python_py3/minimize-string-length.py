# Time:  O(n)
# Space: O(1)

# hash table
class Solution(object):
    def minimizedStringLength(self, s):
        """
        """
        return len(set(s))
