class Solution:
    def maxOperations(self, s):
        n = len(s)
        pref = [0] * (n + 1)
        for j in range(n):
            pref[j + 1] = pref[j] + (s[j] == '1')
        total = 0
        for j in range(n - 1):
            if s[j] == '1' and s[j + 1] == '0':
                total += pref[j + 1]
        return total
