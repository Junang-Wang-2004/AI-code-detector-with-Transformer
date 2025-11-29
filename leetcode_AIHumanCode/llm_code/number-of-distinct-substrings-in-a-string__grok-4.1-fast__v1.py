class Solution:
    def countDistinct(self, s):
        length = len(s)
        suffixes = sorted(range(length), key=lambda idx: s[idx:])
        commons = [0] * length
        for k in range(1, length):
            p = suffixes[k - 1]
            q = suffixes[k]
            m = 0
            while p + m < length and q + m < length and s[p + m] == s[q + m]:
                m += 1
            commons[k] = m
        result = 0
        for i in range(length):
            result += length - suffixes[i] - commons[i]
        return result
