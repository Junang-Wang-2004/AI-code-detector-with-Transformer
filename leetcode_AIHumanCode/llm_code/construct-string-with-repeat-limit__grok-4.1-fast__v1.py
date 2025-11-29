class Solution:
    def repeatLimitedString(self, s, repeatLimit):
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        res = []
        prev = -1
        cnt = 0
        while True:
            found = False
            for i in range(25, -1, -1):
                if freq[i] > 0 and (i != prev or cnt < repeatLimit):
                    res.append(chr(i + ord('a')))
                    freq[i] -= 1
                    if i == prev:
                        cnt += 1
                    else:
                        prev = i
                        cnt = 1
                    found = True
                    break
            if not found:
                break
        return ''.join(res)
