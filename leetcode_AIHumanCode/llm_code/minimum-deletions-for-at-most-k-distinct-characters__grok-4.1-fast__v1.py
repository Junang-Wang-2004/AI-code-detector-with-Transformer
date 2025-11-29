class Solution(object):
    def minDeletion(self, s, k):
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        positives = sorted(x for x in freq if x > 0)
        m = len(positives)
        if m <= k:
            return 0
        return sum(positives[:m - k])
