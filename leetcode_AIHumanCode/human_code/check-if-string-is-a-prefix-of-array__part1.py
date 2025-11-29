# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isPrefixString(self, s, words):
        """
        """
        i = j = 0
        for c in s:
            if i == len(words) or words[i][j] != c:
                return False 
            j += 1
            if j == len(words[i]):
                i += 1
                j = 0
        return j == 0


