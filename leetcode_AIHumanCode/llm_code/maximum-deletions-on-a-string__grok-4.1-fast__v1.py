class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1:
            return n
        MOD1 = 10**9 + 7
        BASE1 = 131
        MOD2 = 10**9 + 9
        BASE2 = 137
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
        def get_h1(left: int, right: int) -> int:
            len_seg = right - left + 1
            h = (pref1[right + 1] - pref1[left] * pow1[len_seg] % MOD1 + MOD1) % MOD1
            return h
        def get_h2(left: int, right: int) -> int:
            len_seg = right - left + 1
            h = (pref2[right + 1] - pref2[left] * pow2[len_seg] % MOD2 + MOD2) % MOD2
            return h
        dp = [1] * n
        for start in range(n - 1, -1, -1):
            curr_max = 1
            max_k = (n - start) // 2
            for k in range(1, max_k + 1):
                mid = start + k
                if get_h1(start, start + k - 1) == get_h1(mid, mid + k - 1) and \
                   get_h2(start, start + k - 1) == get_h2(mid, mid + k - 1):
                    curr_max = max(curr_max, 1 + dp[mid])
            dp[start] = curr_max
        return dp[0]
