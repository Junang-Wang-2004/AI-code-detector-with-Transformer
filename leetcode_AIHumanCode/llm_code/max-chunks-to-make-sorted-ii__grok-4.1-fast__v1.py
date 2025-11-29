class Solution:
    def maxChunksToSorted(self, arr):
        chunks = 0
        max_reach = -1
        for i, val in enumerate(arr):
            if val > max_reach:
                max_reach = val
            if max_reach == i:
                chunks += 1
        return chunks
