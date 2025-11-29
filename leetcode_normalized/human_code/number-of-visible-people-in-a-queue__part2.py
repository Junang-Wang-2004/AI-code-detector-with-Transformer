class C1(object):

    def canSeePersonsCount(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = []
        for v3 in reversed(range(len(a1))):
            v4 = 0
            while v2 and a1[v2[-1]] < a1[v3]:
                v2.pop()
                v4 += 1
            v1[v3] = v4 + 1 if v2 else v4
            if v2 and a1[v2[-1]] == a1[v3]:
                v2.pop()
            v2.append(v3)
        return v1
