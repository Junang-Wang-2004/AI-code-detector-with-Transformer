class C1(object):

    def decodeAtIndex(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in a1:
            if v2.isdigit():
                v1 *= int(v2)
            else:
                v1 += 1
        for v2 in reversed(a1):
            a2 %= v1
            if a2 == 0 and v2.isalpha():
                return v2
            if v2.isdigit():
                v1 /= int(v2)
            else:
                v1 -= 1
