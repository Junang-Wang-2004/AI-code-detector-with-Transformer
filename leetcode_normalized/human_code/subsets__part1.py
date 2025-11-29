class C1(object):

    def subsets(self, a1):
        """
        """
        a1.sort()
        v1 = [[]]
        for v2 in range(len(a1)):
            v3 = len(v1)
            for v4 in range(v3):
                v1.append(list(v1[v4]))
                v1[-1].append(a1[v2])
        return v1
