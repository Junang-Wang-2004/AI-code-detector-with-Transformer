class C1(object):

    def visibleMountains(self, a1):
        """
        """

        def is_covered(a1, a2):
            v1, v2 = a1
            v3, v4 = a2
            return v3 - v4 <= v1 - v2 and v1 + v2 <= v3 + v4
        a1.sort()
        v1 = []
        for v2 in range(len(a1)):
            while v1 and is_covered(a1[v1[-1]], a1[v2]):
                v1.pop()
            if (v2 - 1 == -1 or a1[v2 - 1] != a1[v2]) and (not v1 or not is_covered(a1[v2], a1[v1[-1]])):
                v1.append(v2)
        return len(v1)
