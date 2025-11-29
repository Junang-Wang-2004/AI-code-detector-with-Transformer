class Solution:
    def countDivisibleSubstrings(self, word):
        vals = []
        a = ord('a')
        for ch in word:
            pos = ord(ch) - a
            vals.append((pos + 1) // 3 + 1)
        n = len(vals)
        total = 0
        for k in range(1, 10):
            freq = {0: 1}
            psum = 0
            for j in range(n):
                psum += vals[j]
                target = psum - k * (j + 1)
                total += freq.get(target, 0)
                freq[target] = freq.get(target, 0) + 1
        return total
