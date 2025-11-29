class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]
        for j in range(1, n):
            prefix[j] = max(prefix[j - 1], arr[j])
        total = 0
        for k in range(n):
            if prefix[k] == k:
                total += 1
        return total
