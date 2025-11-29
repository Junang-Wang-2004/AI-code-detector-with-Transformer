class Solution:
    def minSwaps(self, data):
        ones = sum(data)
        n = len(data)
        if ones == 0:
            return 0
        curr = sum(data[:ones])
        best = curr
        for j in range(ones, n):
            curr += data[j] - data[j - ones]
            best = max(best, curr)
        return ones - best
