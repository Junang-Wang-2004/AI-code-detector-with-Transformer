# Time:  O(n)
# Space: O(1)

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        """
        return 1+max(s.count(' ') for s in sentences)
