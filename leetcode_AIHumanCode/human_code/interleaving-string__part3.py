# Time:  O(m * n)
# Space: O(m * n)
# Recursive + Hash
class Solution3(object):
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        self.match = {}
        if len(s1) + len(s2) != len(s3):
            return False
        return self.isInterleaveRecu(s1, s2, s3, 0, 0, 0)

    def isInterleaveRecu(self, s1, s2, s3, a, b, c):
        if repr([a, b]) in list(self.match.keys()):
            return self.match[repr([a, b])]

        if c == len(s3):
            return True

        result = False
        if a < len(s1) and s1[a] == s3[c]:
            result = result or self.isInterleaveRecu(s1, s2, s3, a + 1, b, c + 1)
        if b < len(s2) and s2[b] == s3[c]:
            result = result or self.isInterleaveRecu(s1, s2, s3, a, b + 1, c + 1)

        self.match[repr([a, b])] = result

        return result

