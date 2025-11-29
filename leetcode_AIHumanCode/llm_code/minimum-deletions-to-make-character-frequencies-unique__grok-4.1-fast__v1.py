class Solution(object):
    def minDeletions(self, s):
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        values = sorted(f for f in freq if f > 0)[::-1]
        occupied = set()
        deletions = 0
        for val in values:
            pos = val
            while pos > 0 and pos in occupied:
                pos -= 1
                deletions += 1
            if pos > 0:
                occupied.add(pos)
        return deletions
