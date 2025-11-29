class C1(object):

    def secondsToRemoveOccurrences(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            if v3 == '0':
                v2 += 1
                continue
            if v2:
                v1 = max(v1 + 1, v2)
        return v1
