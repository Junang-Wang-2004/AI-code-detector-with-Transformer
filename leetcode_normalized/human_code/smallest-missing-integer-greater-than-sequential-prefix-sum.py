class C1(object):

    def missingInteger(self, a1):
        """
        """
        v1 = a1[0]
        for v2 in range(1, len(a1)):
            if a1[v2] != a1[v2 - 1] + 1:
                break
            v1 += a1[v2]
        v3 = set(a1)
        while v1 in v3:
            v1 += 1
        return v1
