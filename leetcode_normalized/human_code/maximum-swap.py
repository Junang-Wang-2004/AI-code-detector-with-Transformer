class C1(object):

    def maximumSwap(self, a1):
        """
        """
        v1 = list(str(a1))
        v2, v3 = (0, 0)
        v4 = len(v1) - 1
        for v5 in reversed(range(len(v1))):
            if v1[v5] > v1[v4]:
                v4 = v5
            elif v1[v4] > v1[v5]:
                v2, v3 = (v5, v4)
        v1[v2], v1[v3] = (v1[v3], v1[v2])
        return int(''.join(v1))
