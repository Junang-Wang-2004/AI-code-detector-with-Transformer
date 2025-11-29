class C1(object):

    def findBuildings(self, a1):
        """
        """
        v1 = []
        for v2 in reversed(range(len(a1))):
            if not v1 or a1[v1[-1]] < a1[v2]:
                v1.append(v2)
        v1.reverse()
        return v1
