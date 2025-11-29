class Solution:
    def lexSmallest(self, s):
        n = len(s)
        MOD = 10**9 + 7
        BASE = 31
        powb = [1] * (n + 1)
        for i in range(1, n + 1):
            powb[i] = powb[i - 1] * BASE % MOD
        fwd = [0] * (n + 1)
        for i in range(n):
            fwd[i + 1] = (fwd[i] * BASE + ord(s[i])) % MOD
        revh = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            revh[i] = (revh[i + 1] * BASE + ord(s[i])) % MOD

        def substr_fwd(l, r):
            if l > r:
                return 0
            le = r - l + 1
            return (fwd[r + 1] - fwd[l] * powb[le] % MOD + MOD) % MOD

        def substr_rev(l, r):
            if l > r:
                return 0
            le = r - l + 1
            return (revh[l] - revh[r + 1] * powb[le] % MOD + MOD) % MOD

        def trans_hash(kk, suf, le):
            if le == 0:
                return 0
            if not suf:
                if le <= kk:
                    return substr_rev(kk - le, kk - 1)
                rem = le - kk
                h1 = substr_rev(0, kk - 1)
                h2 = substr_fwd(kk, kk + rem - 1)
                return (h1 * powb[rem] % MOD + h2) % MOD
            else:
                pl = n - kk
                if le <= pl:
                    return substr_fwd(0, le - 1)
                rem = le - pl
                h1 = substr_fwd(0, pl - 1)
                h2 = substr_rev(n - rem, n - 1)
                return (h1 * powb[rem] % MOD + h2) % MOD

        def char_at(kk, suf, p):
            if not suf:
                return s[kk - 1 - p] if p < kk else s[p]
            ss = n - kk
            return s[p] if p < ss else s[n - 1 - (p - ss)]

        def first_diff(k1, s1, k2, s2):
            lo, hi = 0, n
            while lo < hi:
                mi = (lo + hi) // 2
                if trans_hash(k1, s1, mi + 1) != trans_hash(k2, s2, mi + 1):
                    hi = mi
                else:
                    lo = mi + 1
            return lo

        def better(k1, s1, k2, s2):
            dp = first_diff(k1, s1, k2, s2)
            if dp == n:
                return False
            return char_at(k1, s1, dp) < char_at(k2, s2, dp)

        mc = min(s)
        bk, bs = 1, False
        for p in range(n):
            if s[p] == mc:
                ck = p + 1
                if better(ck, False, bk, bs):
                    bk, bs = ck, False
        for ck in range(1, n + 1):
            if s[n - ck] < s[n - 1]:
                continue
            if better(ck, True, bk, bs):
                bk, bs = ck, True
        if not bs:
            return s[:bk][::-1] + s[bk:]
        return s[:n - bk] + s[n - bk:][::-1]
