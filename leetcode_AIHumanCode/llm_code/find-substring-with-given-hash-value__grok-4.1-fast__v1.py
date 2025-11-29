class Solution:
    def subStrHash(self, s, power, modulo, k, hashValue):
        n = len(s)
        if n < k:
            return ""
        high_pow = pow(power, k - 1, modulo)
        window_hash = 0
        for j in range(k):
            window_hash = (window_hash * power + ord(s[j]) - 96) % modulo
        if window_hash == hashValue:
            return s[:k]
        for pos in range(1, n - k + 1):
            window_hash = (window_hash - (ord(s[pos - 1]) - 96) * high_pow) % modulo
            window_hash = (window_hash * power + ord(s[pos + k - 1]) - 96) % modulo
            if window_hash == hashValue:
                return s[pos:pos + k]
        return ""
