class Solution:
    def findOcurrences(self, text, first, second):
        words = text.split()
        res = []
        n = len(words)
        for idx in range(n - 2):
            if words[idx] == first and words[idx + 1] == second:
                res.append(words[idx + 2])
        return res
