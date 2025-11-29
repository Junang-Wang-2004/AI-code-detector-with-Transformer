class C1(object):

    def minOperations(self, a1):
        """
        """
        v1 = 0
        for v2 in a1:
            if v2 == '../':
                if v1 > 0:
                    v1 -= 1
            elif v2 != './':
                v1 += 1
        return v1
