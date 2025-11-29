# Time:  O(m * n)
# Space: O(n)
class Solution2(object):
    # @return a boolean
    def isMatch(self, s, p):
        k = 2
        result = [[False for j in range(len(p) + 1)] for i in range(k)]

        result[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-1]
        for i in range(1,len(s) + 1):
            result[i % k][0] = False
            for j in range(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i % k][j] = result[(i-1) % k][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    result[i % k][j] = result[i % k][j-1] or result[(i-1) % k][j]

        return result[len(s) % k][len(p)]


# dp
