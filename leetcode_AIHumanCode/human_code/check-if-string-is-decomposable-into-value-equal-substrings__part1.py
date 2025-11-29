# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isDecomposable(self, s):
        """
        """
        if len(s)%3 != 2:
            return False
        for left in range(0, len(s), 3):
            if any(s[i] != s[i-1] for i in range(left+1, min(left+3, len(s)))):
                break            
        for right in reversed(range(left+1, len(s), 3)):
            if any(s[i] != s[i+1] for i in reversed(range(max(right-2, left), right))):
                break
        return right-left == 1


