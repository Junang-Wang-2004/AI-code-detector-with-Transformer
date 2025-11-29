class Solution:
    def compress(self, chars):
        pos = 0
        i = 0
        n = len(chars)
        while i < n:
            j = i
            while j < n and chars[j] == chars[i]:
                j += 1
            chars[pos] = chars[i]
            pos += 1
            cnt = j - i
            if cnt > 1:
                for d in str(cnt):
                    chars[pos] = d
                    pos += 1
            i = j
        return pos
