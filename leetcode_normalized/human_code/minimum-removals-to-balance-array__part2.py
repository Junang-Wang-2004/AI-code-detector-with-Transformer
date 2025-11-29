class C1(object):

    def minRemoval(self, a1, a2):
        """
        """
        a1.sort()
        v1 = v2 = 0
        for v3 in range(len(a1)):
            while a1[v2] * a2 < a1[v3]:
                v2 += 1
            v1 = max(v1, v3 - v2 + 1)
        return len(a1) - v1
