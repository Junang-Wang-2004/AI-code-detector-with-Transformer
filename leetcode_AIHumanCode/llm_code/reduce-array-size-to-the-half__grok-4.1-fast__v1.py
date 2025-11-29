from collections import Counter

class Solution:
    def minSetSize(self, arr):
        frequencies = sorted(Counter(arr).values(), reverse=True)
        half = (len(arr) + 1) // 2
        removed = 0
        covered = 0
        for freq in frequencies:
            covered += freq
            removed += 1
            if covered >= half:
                return removed
        return removed
