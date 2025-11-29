class C1(object):

    def minimumAbsDifference(self, a1):
        """
        """
        v1 = []
        v2 = float('inf')
        a1.sort()
        for v3 in range(len(a1) - 1):
            v4 = a1[v3 + 1] - a1[v3]
            if v4 < v2:
                v2 = v4
                v1 = [[a1[v3], a1[v3 + 1]]]
            elif v4 == v2:
                v1.append([a1[v3], a1[v3 + 1]])
        return v1
