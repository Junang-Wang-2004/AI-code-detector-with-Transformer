# Time:  O(n * k), k is the length of the common prefix
# Space: O(k)
class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        """
        prefix = ""
        
        for chars in zip(*strs):
            if all(c == chars[0] for c in chars):
                prefix += chars[0]
            else:
                return prefix
            
        return prefix
