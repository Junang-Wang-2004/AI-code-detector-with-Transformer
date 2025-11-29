class Solution:
    def isFascinating(self, n):
        vals = [n, n * 2, n * 3]
        freq = [0] * 10
        for val in vals:
            cur = val
            while cur > 0:
                digit = cur % 10
                freq[digit] += 1
                cur //= 10
        if freq[0] > 0:
            return False
        for i in range(1, 10):
            if freq[i] != 1:
                return False
        return True
