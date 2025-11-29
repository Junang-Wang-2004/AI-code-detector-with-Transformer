class Solution:
    def numberOfSubstrings(self, s):
        n = len(s)
        freqs = {}
        for ch in s:
            freqs[ch] = freqs.get(ch, 0) + 1
        sum_squares = 0
        for val in freqs.values():
            sum_squares += val * val
        return (sum_squares + n) // 2
