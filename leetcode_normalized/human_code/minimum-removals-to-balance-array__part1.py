class C1(object):

    def minRemoval(self, a1, a2):
        """
        """
        a1.sort()
        v1 = 0
        for v2 in range(len(a1)):
            if a1[v1] * a2 < a1[v2]:
                v1 += 1
        return v1
