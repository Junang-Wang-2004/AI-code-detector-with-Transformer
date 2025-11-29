# Time:  O(n)
# Space: O(1)

class Solution(object):
    def toLowerCase(self, str):
        """
        """
        return "".join([chr(ord('a')+ord(c)-ord('A')) 
                        if 'A' <= c <= 'Z' else c for c in str])

