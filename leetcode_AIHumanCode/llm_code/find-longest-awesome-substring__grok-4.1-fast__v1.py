class Solution:
    def longestAwesome(self, s):
        n = len(s)
        seen = {0: -1}
        max_length = 0
        parity = 0
        for i in range(n):
            digit = int(s[i])
            parity ^= 1 << digit
            max_length = max(max_length, i - seen.get(parity, n))
            for bit in range(10):
                flipped = parity ^ (1 << bit)
                max_length = max(max_length, i - seen.get(flipped, n))
            if parity not in seen:
                seen[parity] = i
        return max_length
