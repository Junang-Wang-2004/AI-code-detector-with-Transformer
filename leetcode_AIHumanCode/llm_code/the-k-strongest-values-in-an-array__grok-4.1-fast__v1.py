class Solution:
    def getStrongest(self, arr, k):
        sorted_arr = sorted(arr)
        median = sorted_arr[(len(sorted_arr) - 1) // 2]
        def strength(val):
            return (abs(val - median), val)
        return sorted(arr, key=strength, reverse=True)[:k]
