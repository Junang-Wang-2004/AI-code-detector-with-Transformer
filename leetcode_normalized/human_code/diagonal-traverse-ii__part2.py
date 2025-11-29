class C1(object):

    def findDiagonalOrder(self, a1):
        """
        """
        v1 = []
        for v2, v3 in enumerate(a1):
            for v4, v5 in enumerate(v3):
                if len(v1) <= v2 + v4:
                    v1.append([])
                v1[v2 + v4].append(v5)
        return [v5 for v3 in v1 for v5 in reversed(v3)]
