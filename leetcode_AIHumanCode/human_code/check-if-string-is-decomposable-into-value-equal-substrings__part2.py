# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def isDecomposable(self, s):
        """
        """
        found, i = False, 0
        while i < len(s):
            l = 1
            for j in range(i+1, min(i+3, len(s))):
                if s[j] != s[i]:
                    break
                l += 1
            if l < 2:
                return False
            if l == 2:
                if found:
                    return False
                found = True
            i += l  
        return found
        

