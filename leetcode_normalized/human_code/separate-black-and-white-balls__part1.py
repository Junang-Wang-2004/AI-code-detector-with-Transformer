class C1(object):

    def minimumSteps(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in range(len(a1)):
            if a1[v3] != '0':
                continue
            v1 += v3 - v2
            v2 += 1
        return v1
