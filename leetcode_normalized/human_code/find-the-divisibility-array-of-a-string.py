class C1(object):

    def divisibilityArray(self, a1, a2):
        """
        """
        v1 = []
        v2 = 0
        for v3 in a1:
            v2 = (v2 * 10 + (ord(v3) - ord('0'))) % a2
            v1.append(int(v2 == 0))
        return v1
