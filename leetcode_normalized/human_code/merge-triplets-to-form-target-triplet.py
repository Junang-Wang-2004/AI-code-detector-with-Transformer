class C1(object):

    def mergeTriplets(self, a1, a2):
        """
        """
        v1 = [0] * 3
        for v2 in a1:
            if all((v2[i] <= a2[i] for v3 in range(3))):
                v1 = [max(v1[v3], v2[v3]) for v3 in range(3)]
        return v1 == a2
