from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        frequencies = sorted(Counter(arr).values())
        remaining_uniques = len(frequencies)
        for freq in frequencies:
            if k >= freq:
                k -= freq
                remaining_uniques -= 1
            else:
                break
        return remaining_uniques
