class C1(object):

    def countLetters(self, a1):
        """
        """
        v1 = len(a1)
        v2 = 0
        for v3 in range(1, len(a1)):
            if a1[v3] == a1[v2]:
                v1 += v3 - v2
            else:
                v2 = v3
        return v1
