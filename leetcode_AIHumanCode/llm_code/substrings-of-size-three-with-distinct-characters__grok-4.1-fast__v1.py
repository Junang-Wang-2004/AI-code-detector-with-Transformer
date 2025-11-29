class Solution(object):
    def countGoodSubstrings(self, s):
        total = 0
        n = len(s)
        for start in range(n - 2):
            a, b, c = s[start], s[start + 1], s[start + 2]
            if a != b and a != c and b != c:
                total += 1
        return total
