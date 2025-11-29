class Solution(object):
    def longestRepeatingSubstring(self, S):
        def has_repeat(length):
            if length == 0:
                return True
            n = len(S)
            mod1 = 10**9 + 7
            base1 = 31
            mod2 = 10**9 + 9
            base2 = 37
            p1 = [1] * (length + 1)
            p2 = [1] * (length + 1)
            for j in range(1, length + 1):
                p1[j] = p1[j - 1] * base1 % mod1
                p2[j] = p2[j - 1] * base2 % mod2
            h1 = 0
            h2 = 0
            hashes = set()
            for j in range(length):
                val = ord(S[j]) - ord('a') + 1
                h1 = (h1 * base1 + val) % mod1
                h2 = (h2 * base2 + val) % mod2
            hashes.add((h1, h2))
            for j in range(length, n):
                oval = ord(S[j - length]) - ord('a') + 1
                nval = ord(S[j]) - ord('a') + 1
                h1 = (h1 - oval * p1[length - 1] % mod1 + mod1) % mod1
                h1 = (h1 * base1 + nval) % mod1
                h2 = (h2 - oval * p2[length - 1] % mod2 + mod2) % mod2
                h2 = (h2 * base2 + nval) % mod2
                pair = (h1, h2)
                if pair in hashes:
                    return True
                hashes.add(pair)
            return False

        l, r = 0, len(S)
        while l < r:
            m = (l + r) // 2
            if has_repeat(m):
                l = m + 1
            else:
                r = m
        return l - 1
