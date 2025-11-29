class C1(object):

    def addSpaces(self, a1, a2):
        """
        """
        v1 = len(a1)
        a1 = list(a1)
        a1.extend([None] * len(a2))
        for v3 in reversed(range(len(a2))):
            for v4 in reversed(range(a2[v3], v1)):
                a1[v4 + 1 + v3] = a1[v4]
            a1[a2[v3] + v3] = ' '
            v1 = a2[v3]
        return ''.join(a1)
