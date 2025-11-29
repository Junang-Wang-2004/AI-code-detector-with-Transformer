class Solution:
    def differByOne(self, words):
        MOD = 10**9 + 7
        BASE = 131
        n = len(words)
        if n < 2:
            return False
        m = len(words[0])
        powb = [1] * (m + 1)
        for j in range(1, m + 1):
            powb[j] = powb[j - 1] * BASE % MOD
        prefixes = []
        for w in words:
            pre = [0] * (m + 1)
            for k in range(m):
                pre[k + 1] = (pre[k] * BASE + (ord(w[k]) - ord('a'))) % MOD
            prefixes.append(pre)
        for pos in range(m):
            seen = {}
            for i in range(n):
                hleft = prefixes[i][pos]
                lenr = m - pos - 1
                temp = prefixes[i][pos + 1] * powb[lenr] % MOD
                hright = (prefixes[i][m] - temp + MOD) % MOD
                comb = (hleft * powb[lenr] % MOD + hright) % MOD
                if comb in seen:
                    for prev in seen[comb]:
                        s1 = words[prev][:pos] + words[prev][pos + 1:]
                        s2 = words[i][:pos] + words[i][pos + 1:]
                        if s1 == s2:
                            return True
                seen.setdefault(comb, []).append(i)
        return False
