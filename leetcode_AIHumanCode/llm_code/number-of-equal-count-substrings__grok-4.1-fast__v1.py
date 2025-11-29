class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        n = len(s)
        total = 0
        for mult in range(1, n // count + 1):
            wlen = mult * count
            freqs = [0] * 26
            matches = 0
            for j in range(n):
                cid = ord(s[j]) - ord('a')
                freqs[cid] += 1
                if freqs[cid] == count:
                    matches += 1
                if j >= wlen:
                    oid = ord(s[j - wlen]) - ord('a')
                    if freqs[oid] == count:
                        matches -= 1
                    freqs[oid] -= 1
                if j >= wlen - 1:
                    if matches == mult:
                        total += 1
        return total
