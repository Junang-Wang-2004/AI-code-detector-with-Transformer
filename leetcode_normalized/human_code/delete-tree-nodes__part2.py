class C1(object):

    def deleteTreeNodes(self, a1, a2, a3):
        """
        """
        v1 = [1] * a1
        for v2 in reversed(range(1, a1)):
            a3[a2[v2]] += a3[v2]
            v1[a2[v2]] += v1[v2] if a3[v2] else 0
        return v1[0]
