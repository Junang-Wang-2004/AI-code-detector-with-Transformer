class Solution:
    def maxSubarrays(self, n, conflictingPairs):
        forbids = [[] for _ in range(n)]
        for p, q in conflictingPairs:
            i = p - 1
            j = q - 1
            if i > j:
                i, j = j, i
            forbids[j].append(i)
        total = 0
        farthest = -1
        for end in range(n):
            for begin in forbids[end]:
                if begin > farthest:
                    farthest = begin
            total += end - farthest
        return total
