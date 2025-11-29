class C1(object):

    def rotatedDigits(self, a1):
        """
        """
        v1, v2 = (set(['3', '4', '7']), set(['2', '5', '6', '9']))
        v3 = 0
        for v4 in range(a1 + 1):
            v5 = set(list(str(v4)))
            if v1 & v5:
                continue
            if v2 & v5:
                v3 += 1
        return v3
