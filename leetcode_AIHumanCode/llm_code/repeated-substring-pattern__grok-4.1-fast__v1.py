class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        for div in range(1, n // 2 + 1):
            if n % div == 0:
                unit = s[:div]
                if unit * (n // div) == s:
                    return True
        return False
