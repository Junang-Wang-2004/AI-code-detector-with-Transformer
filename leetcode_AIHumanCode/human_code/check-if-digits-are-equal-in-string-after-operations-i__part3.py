# Time:  O(n^2)
# Space: O(1)
class Solution3(object):
    def hasSameDigits(self, s):
        """
        """
        s = list(map(int, s))
        for l in reversed(range(3, len(s)+1)):
            for i in range(l-1):
                s[i] = (s[i]+s[i+1])%10
        return s[0] == s[1]
