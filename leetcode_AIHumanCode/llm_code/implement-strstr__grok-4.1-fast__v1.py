class Solution:
    def strStr(self, source, target):
        if not target:
            return 0
        slen, tlen = len(source), len(target)
        for pos in range(slen - tlen + 1):
            j = 0
            while j < tlen and source[pos + j] == target[j]:
                j += 1
            if j == tlen:
                return pos
        return -1
