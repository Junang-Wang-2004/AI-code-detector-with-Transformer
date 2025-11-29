class C1(object):

    def kthCharacter(self, a1, a2):
        """
        """
        v1 = 0
        a1 -= 1
        for v3 in range(min(len(a2), a1.bit_length())):
            if a1 & 1 << v3:
                v1 = (v1 + a2[v3]) % 26
        return chr(ord('a') + v1)
