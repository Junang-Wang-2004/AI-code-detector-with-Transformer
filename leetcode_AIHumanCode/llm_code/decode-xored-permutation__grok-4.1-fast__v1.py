class Solution:
    def decode(self, encoded):
        n = len(encoded) + 1
        def xor_to_n(m):
            rem = m % 4
            if rem == 0:
                return m
            elif
