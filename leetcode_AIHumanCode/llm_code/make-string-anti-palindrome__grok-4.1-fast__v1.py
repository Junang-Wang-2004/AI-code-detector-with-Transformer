class Solution:
    def makeAntiPalindrome(self, s):
        n = len(s)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        if max(freq) > n // 2:
            return "-1"
        res = [0] * n

        def pick(avoid=-1):
            for j in range(26):
                if freq[j] > 0 and j != avoid:
                    return j
            return -1

        for i in range(n // 2):
            l = pick()
            res[i] = l
            freq[l] -= 1
            r = pick(l)
            res[n - 1 - i] = r
            freq[r] -= 1
        if n % 2:
            res[n // 2] = pick()
        return "".join(chr(ord('a') + x) for x in res)
