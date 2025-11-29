class Solution:
    def findPattern(self, stream, pattern):
        n = len(pattern)
        if n == 0:
            return 0

        lps = [0] * n
        length = 0
        i = 1
        while i < n:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        pos = 0
        match_len = 0
        while True:
            ch = next(stream)
            while match_len > 0 and pattern[match_len] != ch:
                match_len = lps[match_len - 1]
            if pattern[match_len] == ch:
                match_len += 1
            if match_len == n:
                return pos - n + 1
            pos += 1
