class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        size = r - l + 1
        ways = [1] * size
        for _ in range(n - 1):
            psum = [0] * (size + 1)
            for j in range(size):
                psum[j + 1] = (psum[j] + ways[j]) % MOD
            ways = psum[:size][::-1]
        return sum(ways) * 2 % MOD
