class Solution:
    def modifyString(self, s):
        chars = list(s)
        length = len(chars)
        for pos in range(length):
            if chars[pos] == '?':
                banned = set()
                if pos > 0:
                    banned.add(chars[pos - 1])
                if pos < length - 1:
                    banned.add(chars[pos + 1])
                for letter in 'abc':
                    if letter not in banned:
                        chars[pos] = letter
                        break
        return ''.join(chars)
