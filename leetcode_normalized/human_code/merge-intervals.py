class C1(object):

    def merge(self, a1):
        """
        """
        a1.sort()
        v1 = []
        for v2 in a1:
            if not v1 or v2[0] > v1[-1][1]:
                v1.append(v2)
            else:
                v1[-1][1] = max(v1[-1][1], v2[1])
        return v1
