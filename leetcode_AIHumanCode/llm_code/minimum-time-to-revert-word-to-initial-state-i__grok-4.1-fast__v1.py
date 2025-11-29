class Solution(object):
    def minimumTimeToInitialState(self, word, k):
        n = len(word)
        MOD1 = 1000000007
        MOD2 = 1000000009
        BASE1 = 131
        BASE2 = 137
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        for i in range(n):
            val = ord(word[i])
            h1[i + 1] = (h1[i] * BASE1 + val) % MOD1
            h2[i + 1] = (h2[i] * BASE2 + val) % MOD2
            p1[i + 1] = p1[i] * BASE1 % MOD1
            p2[i + 1] = p2[i] * BASE2 % MOD2
        def get_hash(left, right):
            v1 = (h1[right] - h1[left] * p1[right - left] % MOD1 + MOD1) % MOD1
            v2 = (h2[right] - h2[left] * p2[right - left] % MOD2 + MOD2) % MOD2
            return v1, v2
        for pos in range(k, n + 1, k):
            length = n - pos
            if get_hash(pos, n) == get_hash(0, length):
                return pos // k
        return (n + k - 1) // k
