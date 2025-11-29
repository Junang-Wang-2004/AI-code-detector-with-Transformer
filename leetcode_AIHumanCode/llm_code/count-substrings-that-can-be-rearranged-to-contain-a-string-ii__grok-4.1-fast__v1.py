class Solution:
    def validSubstringCount(self, word1, word2):
        n = len(word1)
        req = [0] * 26
        need = 0
        a_ord = ord('a')
        for ch in word2:
            idx = ord(ch) - a_ord
            if req[idx] == 0:
                need += 1
            req[idx] += 1
        remain = req[:]
        lack = need
        total = 0
        begin = 0
        for pos in range(n):
            idx = ord(word1[pos]) - a_ord
            remain[idx] -= 1
            if remain[idx] == 0:
                lack -= 1
            while lack == 0:
                total += n - pos
                idx_left = ord(word1[begin]) - a_ord
                if remain[idx_left] == 0:
                    lack += 1
                remain[idx_left] += 1
                begin += 1
        return total
