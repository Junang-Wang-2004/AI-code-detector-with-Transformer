class Solution:
    def numWays(self, s):
        MOD = 10**9 + 7
        n = len(s)
        total = sum(c == '1' for c in s)
        if total % 3:
            return 0
        target = total // 3
        if target == 0:
            return (n - 1) * (n - 2) // 2 % MOD
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (s[i] == '1')
        cnt_first = pref.count(target)
        cnt_second = pref.count(2 * target)
        return cnt_first * cnt_second % MOD
