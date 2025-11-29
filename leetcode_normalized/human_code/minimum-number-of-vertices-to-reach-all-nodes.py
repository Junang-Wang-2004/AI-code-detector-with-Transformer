class C1(object):

    def findSmallestSetOfVertices(self, a1, a2):
        """
        """
        v1 = []
        v2 = set()
        for v3, v4 in a2:
            v2.add(v4)
        for v5 in range(a1):
            if v5 not in v2:
                v1.append(v5)
        return v1
