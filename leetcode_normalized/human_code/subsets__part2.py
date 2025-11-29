class C1(object):

    def subsets(self, a1):
        """
        """
        v1 = []
        v2, v3 = (0, 1 << len(a1))
        a1.sort()
        while v2 < v3:
            v4 = []
            for v5 in range(len(a1)):
                if v2 & 1 << v5:
                    v4.append(a1[v5])
            v1.append(v4)
            v2 += 1
        return v1
