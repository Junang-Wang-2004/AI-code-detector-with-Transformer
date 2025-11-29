class Solution:
    def reverseWords(self, s):
        res = []
        i = 0
        length = len(s)
        while i < length:
            if s[i] == ' ':
                res.append(' ')
                i += 1
                continue
            j = i
            while j < length and s[j] != ' ':
                j += 1
            for k in range(j - 1, i - 1, -1):
                res.append(s[k])
            i = j
        return ''.join(res)
