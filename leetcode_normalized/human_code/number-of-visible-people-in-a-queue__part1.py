class C1(object):

    def canSeePersonsCount(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = []
        for v3, v4 in enumerate(a1):
            while v2 and a1[v2[-1]] < v4:
                v1[v2.pop()] += 1
            if v2:
                v1[v2[-1]] += 1
            if v2 and a1[v2[-1]] == v4:
                v2.pop()
            v2.append(v3)
        return v1
