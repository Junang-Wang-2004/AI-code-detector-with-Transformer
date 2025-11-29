# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def isPrefixString(self, s, words):
        """
        """
        i = 0
        for word in words:
            for c in word:
                if i == len(s) or s[i] != c:
                    return False
                i += 1
            if i == len(s):
                return True
        return False
