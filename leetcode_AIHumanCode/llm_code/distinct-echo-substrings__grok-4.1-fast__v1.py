class Solution:
    def distinctEchoSubstrings(self, text):
        n = len(text)
        if n < 2:
            return 0
        MOD1 = 1000000007
        BASE1 = 31
        MOD2 = 1000000009
        BASE2 = 37
        prefix1 = [0] * (n + 1)
        prefix2 = [0] * (n + 1)
        power1 = [1] * (n + 1)
        power2 = [1] * (n + 1)
        for pos in range(n):
            val = ord(text[pos]) - ord('a') + 1
            prefix1[pos + 1] = (prefix1[pos] * BASE1 + val) % MOD1
            prefix2[pos + 1] = (prefix2[pos] * BASE2 + val) % MOD2
            power1[pos + 1] = (power1[pos] * BASE1) % MOD1
            power2[pos + 1] = (power2[pos] * BASE2) % MOD2
        
        def substr_hash1(left, right):
            res = (prefix1[right] - prefix1[left] * power1[right - left] % MOD1 + MOD1) % MOD1
            return res
        
        def substr_hash2(left, right):
            res = (prefix2[right] - prefix2[left] * power2[right - left] % MOD2 + MOD2) % MOD2
            return res
        
        unique = set()
        for sz in range(1, (n // 2) + 1):
            for begin in range(n - 2 * sz + 1):
                left_h1 = substr_hash1(begin, begin + sz)
                right_h1 = substr_hash1(begin + sz, begin + 2 * sz)
                left_h2 = substr_hash2(begin, begin + sz)
                right_h2 = substr_hash2(begin + sz, begin + 2 * sz)
                if left_h1 == right_h1 and left_h2 == right_h2:
                    unique.add((left_h1, left_h2))
        return len(unique)
