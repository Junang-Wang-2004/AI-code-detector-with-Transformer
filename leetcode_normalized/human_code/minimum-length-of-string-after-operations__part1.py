class C1(object):

    def minimumLength(self, a1):
        """
        """
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        return sum((2 - v2 % 2 for v2 in v1 if v2))
