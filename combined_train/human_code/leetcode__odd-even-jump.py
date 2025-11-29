class C1(object):

    def oddEvenJumps(self, a1):
        """
        """

        def findNext(a1):
            v1 = [None] * len(a1)
            v2 = []
            for v3 in a1:
                while v2 and v2[-1] < v3:
                    v1[v2.pop()] = v3
                v2.append(v3)
            return v1
        v1 = sorted(list(range(len(a1))), key=lambda i: a1[i])
        v2 = findNext(v1)
        v1.sort(key=lambda i: -a1[i])
        v3 = findNext(v1)
        v4, v5 = ([False] * len(a1), [False] * len(a1))
        v4[-1], v5[-1] = (True, True)
        for v6 in reversed(range(len(a1) - 1)):
            if v2[v6]:
                v4[v6] = v5[v2[v6]]
            if v3[v6]:
                v5[v6] = v4[v3[v6]]
        return sum(v4)
