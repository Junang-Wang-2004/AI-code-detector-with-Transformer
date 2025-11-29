class C1(object):

    def findSmallestRegion(self, a1, a2, a3):
        """
        """
        v1 = {region[i]: region[0] for v2 in a1 for v3 in range(1, len(v2))}
        v4 = {a2}
        while a2 in v1:
            a2 = v1[a2]
            v4.add(a2)
        while a3 not in v4:
            a3 = v1[a3]
        return a3
