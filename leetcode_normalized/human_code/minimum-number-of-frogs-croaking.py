class C1(object):

    def minNumberOfFrogs(self, a1):
        """
        """
        v1 = 'croak'
        v2 = [0] * len(v1)
        v3 = 0
        for v4 in a1:
            v5 = v1.find(v4)
            v2[v5] += 1
            if v2[v5 - 1]:
                v2[v5 - 1] -= 1
            elif v5 == 0:
                v3 += 1
            else:
                return -1
        return v3 if v3 == v2[-1] else -1
