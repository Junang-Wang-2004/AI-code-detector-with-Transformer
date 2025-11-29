class Solution:
    def findPattern(self, stream, pattern):
        pat_len = len(pattern)
        if pat_len == 0:
            return 0

        fail = [0] * pat_len
        match_len = 0
        k = 1
        while k < pat_len:
            if pattern[k] == pattern[match_len]:
                match_len += 1
                fail[k] = match_len
                k += 1
            else:
                if match_len != 0:
                    match_len = fail[match_len - 1]
                else:
                    fail[k] = 0
                    k += 1

        pos = 0
        state = 0
        while True:
            ch = next(stream)
            while state > 0 and pattern[state] != ch:
                state = fail[state - 1]
            if pattern[state] == ch:
                state += 1
            if state == pat_len:
                return pos - pat_len + 1
            pos += 1
