# Time:  O(m * n)
# Space: O(m * n)
class Solution3(object):
    # @return a boolean
    def isMatch(self, s, p):
        result = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]

        result[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-1]
        for i in range(1,len(s) + 1):
            result[i][0] = False
            for j in range(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i][j] = result[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    result[i][j] = result[i][j-1] or result[i-1][j]

        return result[len(s)][len(p)]


# recursive, slowest, TLE
class Solution4(object):
    # @return a boolean
    def isMatch(self, s, p):
        if not p or not s:
            return not s and not p

        if p[0] != '*':
            if p[0] == s[0] or p[0] == '?':
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s) > 0:
                if self.isMatch(s, p[1:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[1:])

