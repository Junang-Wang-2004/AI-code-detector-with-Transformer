class C1(object):

    def findMissingRanges(self, a1, a2, a3):
        """
        """

        def getRange(a1, a2):
            if a1 == a2:
                return '{}'.format(a1)
            else:
                return '{}->{}'.format(a1, a2)
        v1 = []
        v2 = a2 - 1
        for v3 in range(len(a1) + 1):
            if v3 == len(a1):
                v4 = a3 + 1
            else:
                v4 = a1[v3]
            if v4 - v2 >= 2:
                v1.append(getRange(v2 + 1, v4 - 1))
            v2 = v4
        return v1
