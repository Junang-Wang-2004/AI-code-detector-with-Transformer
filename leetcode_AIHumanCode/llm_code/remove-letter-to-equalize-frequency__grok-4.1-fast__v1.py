class Solution:
    def equalFrequency(self, word):
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        for i in range(26):
            if freq[i] == 0:
                continue
            freq[i] -= 1
            vals = [f for f in freq if f > 0]
            if len(set(vals)) == 1:
                return True
            freq[i] += 1
        return False
