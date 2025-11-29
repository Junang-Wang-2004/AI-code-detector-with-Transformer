class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        changes = [0] * (n + 1)
        for start, end, direction in shifts:
            delta = 2 * direction - 1
            changes[start] += delta
            if end + 1 <= n:
                changes[end + 1] -= delta
        res = []
        offset = 0
        base = ord('a')
        for i in range(n):
            offset += changes[i]
            shifted = (ord(s[i]) - base + offset) % 26
            res.append(chr(base + shifted))
        return ''.join(res)
