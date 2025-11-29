class C1(object):

    def shiftingLetters(self, a1, a2):
        """
        """
        v1 = []
        v2 = sum(a2) % 26
        for v3, v4 in enumerate(a1):
            v5 = ord(v4) - ord('a')
            v1.append(chr(ord('a') + (v5 + v2) % 26))
            v2 = (v2 - a2[v3]) % 26
        return ''.join(v1)
