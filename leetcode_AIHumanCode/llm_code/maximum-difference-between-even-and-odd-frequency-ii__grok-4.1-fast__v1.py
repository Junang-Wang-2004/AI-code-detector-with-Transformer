class Solution(object):
    def maxDifference(self, s, k):
        chars = list(set(s))
        n = len(s)
        answer = float('-inf')
        for idx1 in range(len(chars)):
            x = chars[idx1]
            for idx2 in range(len(chars)):
                y = chars[idx2
