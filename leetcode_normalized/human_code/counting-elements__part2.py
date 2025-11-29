class C1(object):

    def countElements(self, a1):
        """
        """
        a1.sort()
        v1, v2 = (0, 1)
        for v3 in range(len(a1) - 1):
            if a1[v3] == a1[v3 + 1]:
                v2 += 1
                continue
            if a1[v3] + 1 == a1[v3 + 1]:
                v1 += v2
            v2 = 1
        return v1
