class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        prefix = [0] * (k + 1)
        for i in range(1, k + 1):
            prefix[i] = prefix[i - 1] + cardPoints[i - 1]
        suffix = [0] * (k + 1)
        for i in range(1, k + 1):
            suffix[i] = suffix[i - 1] + cardPoints[n - i]
        res = 0
        for i in range(k + 1):
            res = max(res, prefix[i] + suffix[k - i])
        return res
