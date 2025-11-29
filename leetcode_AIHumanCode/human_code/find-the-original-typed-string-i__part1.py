# Time:  O(n)
# Space: O(1)

# array
class Solution(object):
    def possibleStringCount(self, word):
        """
        """
        return len(word)-sum(word[i] != word[i+1] for i in range(len(word)-1))


