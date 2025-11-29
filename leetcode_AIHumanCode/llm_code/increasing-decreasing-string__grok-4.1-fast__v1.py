import string

class Solution:
    def sortString(self, s):
        letters = string.ascii_lowercase
        freqs = [0] * 26
        for ch in s:
            freqs[ord(ch) - 97] += 1
        built = []
        up = True
        slen = len(s)
        while len(built) < slen:
            if up:
                for j in range(26):
                    if freqs[j] > 0:
                        built.append(letters[j])
                        freqs[j] -= 1
            else:
                for j in range(25, -1, -1):
                    if freqs[j] > 0:
                        built.append(letters[j])
                        freqs[j] -= 1
            up = not up
        return "".join(built)
