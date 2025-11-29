class C1(object):

    def findScore(self, a1):
        """
        """
        v1 = list(range(len(a1)))
        v1.sort(key=lambda x: (a1[x], x))
        v2 = [False] * len(a1)
        v3 = 0
        for v4 in v1:
            if v2[v4]:
                continue
            v2[v4] = True
            if v4 - 1 >= 0:
                v2[v4 - 1] = True
            if v4 + 1 < len(v2):
                v2[v4 + 1] = True
            v3 += a1[v4]
        return v3
