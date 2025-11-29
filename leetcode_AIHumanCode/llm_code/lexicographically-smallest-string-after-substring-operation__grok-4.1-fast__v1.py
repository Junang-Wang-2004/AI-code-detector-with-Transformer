class Solution:
    def smallestString(self, s):
        chars = list(s)
        n = len(chars)
        idx = 0
        decrementing = False
        while idx < n:
            if decrementing:
                if chars[idx] == 'a':
                    break
                chars[idx] = chr(ord(chars[idx]) - 1)
            else:
                if chars[idx] != 'a':
                    decrementing = True
                    chars[idx] = chr(ord(chars[idx]) - 1)
            idx += 1
        if not decrementing:
            chars[-1] = 'z'
        return ''.join(chars)
