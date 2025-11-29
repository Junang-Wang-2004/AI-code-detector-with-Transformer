class Solution(object):
    def findGoodStrings(self, n, s1, s2, evil):
        MOD = 10**9 + 7
        m = len(evil)
        pi = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and evil[i] != evil[j]:
                j = pi[j - 1]
            if evil[i] == evil[j]:
                j += 1
            pi[i] = j
        trans = [[0] * 26 for _ in range(m + 1)]
        for state in range(m + 1):
            for ci in range(26):
                ch = chr(ord('a') + ci)
                if state < m and evil[state] == ch:
                    trans[state][ci] = state + 1
                else:
                    fail = pi[state - 1] if state > 0 else 0
                    trans[state][ci] = trans[fail][ci]
        memo = {}
        def count(pos, tight_lo, tight_hi, state):
            if pos == n:
                return 1
            key = (pos, tight_lo, tight_hi, state)
            if key in memo:
                return memo[key]
            total = 0
            low_lim = ord(s1[pos]) - ord('a') if tight_lo else 0
            up_lim = ord(s2[pos]) - ord('a') if tight_hi else 25
            for ci in range(low_lim, up_lim + 1):
                new_lo = tight_lo and ci == low_lim
                new_hi = tight_hi and ci == up_lim
                next_state = trans[state][ci]
                if next_state == m:
                    continue
                total = (total + count(pos + 1, new_lo, new_hi, next_state)) % MOD
            memo[key] = total
            return total
        return count(0, True, True, 0)
