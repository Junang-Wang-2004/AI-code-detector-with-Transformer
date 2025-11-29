class Solution:
    def minChanges(self, n, k):
        changes = 0
        while n or k:
            bit_k = k & 1
            bit_n = n & 1
            if bit_k:
                if not bit_n:
                    return -1
            elif bit_n:
                changes += 1
            n >>= 1
            k >>= 1
        return changes
