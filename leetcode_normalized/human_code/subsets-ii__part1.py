class C1(object):

    def subsetsWithDup(self, a1):
        """
        """
        a1.sort()
        v1 = [[]]
        v2 = 0
        for v3 in range(len(a1)):
            v4 = len(v1)
            for v5 in range(v4):
                if v3 == 0 or a1[v3] != a1[v3 - 1] or v5 >= v2:
                    v1.append(list(v1[v5]))
                    v1[-1].append(a1[v3])
            v2 = v4
        return v1
