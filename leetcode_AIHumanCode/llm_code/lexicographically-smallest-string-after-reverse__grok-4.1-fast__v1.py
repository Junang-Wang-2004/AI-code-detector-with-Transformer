class Solution:
    def lexSmallest(self, s):
        n = len(s)
        if n < 2:
            return s
        MOD = 998244353
        BASE = 31
        ords = [ord(c) for c in s]
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = (pre[i] * BASE + ords[i]) % MOD
        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf[i] = (suf[i + 1] * BASE + ords[i]) % MOD
        power = [1] * (n + 1)
        for i in range(1, n + 1):
            power[i] = power[i - 1] * BASE % MOD

        def substr_fwd(l, r):
            if l > r:
                return 0
            h = (pre[r + 1] - pre[l] * power[r - l + 1] % MOD + MOD) % MOD
            return h

        def substr_rev(l, r):
            if l > r:
                return 0
            h = (suf[l] - suf[r + 1] * power[r - l + 1] % MOD + MOD) % MOD
            return h

        def prefix_hash(rev_len, query_len):
            if query_len <= rev_len:
                return substr_rev(rev_len - query_len, rev_len - 1)
            rh = substr_rev(0, rev_len - 1)
            ah = substr_fwd(rev_len, query_len - 1)
            return (rh * power[query_len - rev_len] + ah) % MOD

        def suffix_hash(rev_len, query_len):
            fixed = n - rev_len
            if query_len <= fixed:
                return substr_fwd(0, query_len - 1)
            fh = substr_fwd(0, fixed - 1) if fixed else 0
            alen = query_len - fixed
            ah = substr_rev(n - alen, n - 1)
            return (fh * power[alen] + ah) % MOD

        def ch_at(rev_len, is_suffix, idx):
            if not is_suffix:
                return s[rev_len - 1 - idx] if idx < rev_len else s[idx]
            fixed = n - rev_len
            return s[idx] if idx < fixed else s[n - 1 - (idx - fixed)]

        def is_strictly_smaller(rl1, suf1, rl2, suf2):
            l, r = 0, n - 1
            while l <= r:
                m = (l + r) // 2
                h1 = suffix_hash(rl1, m + 1) if suf1 else prefix_hash(rl1, m + 1)
                h2 = suffix_hash(rl2, m + 1) if suf2 else prefix_hash(rl2, m + 1)
                if h1 == h2:
                    l = m + 1
                else:
                    r = m - 1
            pos = l
            if pos == n:
                return False
            return ch_at(rl1, suf1, pos) < ch_at(rl2, suf2, pos)

        min_char = min(s)
        opt_len = 1
        opt_suffix = False
        for pos in range(n):
            if s[pos] == min_char:
                clen = pos + 1
                if is_strictly_smaller(clen, False, opt_len, opt_suffix):
                    opt_len = clen
                    opt_suffix = False
        for clen in range(1, n + 1):
            if s[n - clen] < s[-1]:
                continue
            if is_strictly_smaller(clen, True, opt_len, opt_suffix):
                opt_len = clen
                opt_suffix = True
        if not opt_suffix:
            return s[:opt_len][::-1] + s[opt_len:]
        return s[:-opt_len] + s[-opt_len:][::-1]
