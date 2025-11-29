# Time:  O(n)
# Space: O(1)
import collections

class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        """
        """
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

