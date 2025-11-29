class C1(object):

    def maximumImportance(self, a1, a2):
        """
        """
        v1 = [0] * a1
        for v2, v3 in a2:
            v1[v2] += 1
            v1[v3] += 1
        v1.sort()
        return sum((i * x for v4, v5 in enumerate(v1, 1)))
