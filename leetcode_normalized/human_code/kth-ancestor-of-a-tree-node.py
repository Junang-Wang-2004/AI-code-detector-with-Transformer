class C1(object):

    def __init__(self, a1, a2):
        """
        """
        v1 = [[p] if p != -1 else [] for v2 in a2]
        v3 = [v1[i] for v4, v2 in enumerate(a2) if v2 != -1]
        v4 = 0
        while v3:
            v5 = []
            for v2 in v3:
                if not v4 < len(v1[v2[v4]]):
                    continue
                v2.append(v1[v2[v4]][v4])
                v5.append(v2)
            v3 = v5
            v4 += 1
        self.__parent = v1

    def getKthAncestor(self, a1, a2):
        """
        """
        v1, v2, v3 = (self.__parent, 0, 1)
        while v3 <= a2:
            if a2 & v3:
                if not v2 < len(v1[a1]):
                    return -1
                a1 = v1[a1][v2]
            v2 += 1
            v3 *= 2
        return a1
