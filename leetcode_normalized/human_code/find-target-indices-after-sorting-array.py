class C1(object):

    def targetIndices(self, a1, a2):
        """
        """
        v1 = sum((x < a2 for v2 in a1))
        return list(range(v1, v1 + sum((v2 == a2 for v2 in a1))))
