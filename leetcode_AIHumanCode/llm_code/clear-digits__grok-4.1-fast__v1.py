class Solution:
    def clearDigits(self, s):
        chars = list(s)
        pos = 0
        for idx in range(len(chars)):
            if 'a' <= chars[idx] <= 'z':
                chars[pos] = chars[idx]
                pos += 1
            elif pos > 0:
                pos -= 1
        return ''.join(chars[:pos])
