class C1(object):

    def visibleMountains(self, a1):
        """
        """
        a1.sort(key=lambda x: (x[0] - x[1], -(x[0] + x[1])))
        v1 = v2 = 0
        for v3 in range(len(a1)):
            if a1[v3][0] + a1[v3][1] <= v2:
                continue
            v2 = a1[v3][0] + a1[v3][1]
            if v3 + 1 == len(a1) or a1[v3 + 1] != a1[v3]:
                v1 += 1
        return v1
