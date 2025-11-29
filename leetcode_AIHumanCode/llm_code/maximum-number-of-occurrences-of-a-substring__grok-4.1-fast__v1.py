class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        k = minSize
        if n < k:
            return 0
        MOD1, BASE1 = 1000000007, 131
        MOD2, BASE2 = 1000000009, 137
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)
        for i in range(n):
            val = ord(s[i]) - ord('a') + 1
            pref1[i + 1] = (pref1[i] * BASE1 + val) % MOD1
            pow1[i + 1] = pow1[i] * BASE1 % MOD1
            pref2[i + 1] = (pref2[i] * BASE2 + val) % MOD2
            pow2[i + 1] = pow2[i] * BASE2 % MOD2
        char_freq = {}
        hash_count = {}
        start = 0
        result = 0
        for end in range(n):
            char_freq[s[end]] = char_freq.get(s[end], 0) + 1
            while end - start + 1 > k:
                char_freq[s[start]] -= 1
                if char_freq[s[start]] == 0:
                    del char_freq[s[start]]
                start += 1
            if end - start + 1 == k and len(char_freq) <= maxLetters:
                lenw = k
                h1 = (pref1[end + 1] - pref1[start] * pow1[lenw] % MOD1 + MOD1) % MOD1
                h2 = (pref2[end + 1] - pref2[start] * pow2[lenw] % MOD2 + MOD2) % MOD2
                hashes = (h1, h2)
                current = hash_count.get(hashes, 0) + 1
                hash_count[hashes] = current
                if current > result:
                    result = current
        return result
