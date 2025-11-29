class Solution:
    def uniqueLetterString(self, S):
        MOD = 10**9 + 7
        n = len(S)
        prev_pos = [-1] * 26
        prev_prev_pos = [-1] * 26
        total = 0
        for pos in range(n):
            char_idx = ord(S[pos]) - ord('A')
            p1 = prev_pos[char_idx]
            p0 = prev_prev_pos[char_idx]
            total = (total + (pos - p1) * (p1 - p0)) % MOD
            prev_prev_pos[char_idx] = p1
            prev_pos[char_idx] = pos
        for ci in range(26):
            p1 = prev_pos[ci]
            p0 = prev_prev_pos[ci]
            total = (total + (n - p1) * (p1 - p0)) % MOD
        return total
