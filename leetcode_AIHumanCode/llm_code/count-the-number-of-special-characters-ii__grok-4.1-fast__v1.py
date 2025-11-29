class Solution(object):
    def numberOfSpecialChars(self, word):
        n = len(word)
        last_lower = [-1] * 26
        first_upper = [n] * 26
        for i, ch in enumerate(word):
            idx = ord(ch.lower()) - ord('a')
            if ch.islower():
                last_lower[idx] = i
            elif ch.isupper():
                first_upper[idx] = min(first_upper[idx], i)
        res = 0
        for k in range(26):
            if (last_lower[k] >= 0 and
                first_upper[k] < n and
                last_lower[k] < first_upper[k]):
                res += 1
        return res
