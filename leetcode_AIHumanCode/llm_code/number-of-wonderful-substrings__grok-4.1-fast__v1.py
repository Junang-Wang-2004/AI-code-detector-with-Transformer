class Solution:
    def wonderfulSubstrings(self, word):
        N = 1 << 10
        freqs = [0] * N
        freqs[0] = 1
        mask = 0
        ans = 0
        for ch in word:
            pos = ord(ch) - ord('a')
            mask ^= 1 << pos
            ans += freqs[mask]
            for i in range(10):
                neigh = mask ^ (1 << i)
                ans += freqs[neigh]
            freqs[mask] += 1
        return ans
