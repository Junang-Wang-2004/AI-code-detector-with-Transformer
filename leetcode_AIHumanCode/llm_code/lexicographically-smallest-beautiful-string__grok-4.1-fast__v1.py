class Solution(object):
    def smallestBeautifulString(self, s, k):
        n = len(s)
        letters = [ord(c) - ord('a') for c in s]
        for p in range(n - 1, -1, -1):
            p1 = letters[p - 1] if p >= 1 else -1
            p2 = letters[p - 2] if p >= 2 else -1
            v = letters[p] + 1
            while v < k and (v == p1 or v == p2):
                v += 1
            if v < k:
                result = letters[:p] + [v]
                for pos in range(p + 1, n):
                    prev = result[pos - 1]
                    prev_prev = result[pos - 2] if pos >= 2 else -1
                    cand = 0
                    while cand == prev or cand == prev_prev:
                        cand += 1
                    result.append(cand)
                return "".join(chr(ord('a') + x) for x in result)
        return ""
