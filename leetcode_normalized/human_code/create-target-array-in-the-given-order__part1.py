class C1(object):

    def createTargetArray(self, a1, a2):
        """
        """
        for v1 in range(len(a1)):
            for v2 in range(v1):
                if a2[v2] >= a2[v1]:
                    a2[v2] += 1
        v3 = [0] * len(a1)
        for v1 in range(len(a1)):
            v3[a2[v1]] = a1[v1]
        return v3
