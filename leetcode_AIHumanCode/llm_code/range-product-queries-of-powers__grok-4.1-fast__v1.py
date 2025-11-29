class Solution:
    def productQueries(self, n, queries):
        MOD = 10**9 + 7
        bit_positions = [i for i in range(64) if n & (1 << i)]
        result = []
        for start, end in queries:
            exponent = sum(bit_positions[start:end + 1])
            result.append(pow(2, exponent, MOD))
        return result
