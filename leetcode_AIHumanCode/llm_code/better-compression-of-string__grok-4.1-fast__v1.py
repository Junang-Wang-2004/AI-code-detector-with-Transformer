class Solution(object):
    def betterCompression(self, compressed):
        freq = [0] * 26
        pos = 0
        n = len(compressed)
        while pos < n:
            ch = compressed[pos]
            let_idx = ord(ch) - ord('a')
            pos += 1
            digits = ''
            while pos < n and compressed[pos].isdigit():
                digits += compressed[pos]
                pos += 1
            if digits:
                freq[let_idx] += int(digits)
        parts = []
        for k in range(26):
            if freq[k] > 0:
                parts.append(chr(ord('a') + k) + str(freq[k]))
        return ''.join(parts)
