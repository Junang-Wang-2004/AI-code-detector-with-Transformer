class Solution:
    def getHint(self, secret, guess):
        bulls = 0
        s_count = [0] * 10
        g_count = [0] * 10
        n = len(secret)
        for i in range(n):
            ds = ord(secret[i]) - ord('0')
            dg = ord(guess[i]) - ord('0')
            if ds == dg:
                bulls += 1
            else:
                s_count[ds] += 1
                g_count[dg] += 1
        cows = sum(min(s_count[j], g_count[j]) for j in range(10))
        return f"{bulls}A{cows}B"
