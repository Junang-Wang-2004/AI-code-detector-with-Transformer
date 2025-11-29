class Solution:
    def rangeBitwiseAnd(self, left, right):
        bits = 0
        while left != right:
            left >>= 1
            right >>= 1
            bits += 1
        return left << bits
