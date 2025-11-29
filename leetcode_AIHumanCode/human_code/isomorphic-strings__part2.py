# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        return self.halfIsom(s, t) and self.halfIsom(t, s)

    def halfIsom(self, s, t):
        lookup = {}
        for i in range(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = t[i]
            elif lookup[s[i]] != t[i]:
                return False
        return True

