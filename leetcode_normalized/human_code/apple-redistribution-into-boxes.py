class C1(object):

    def minimumBoxes(self, a1, a2):
        """
        """
        a2.sort(reverse=True)
        v1 = sum(a1)
        for v2 in range(len(a2)):
            v1 -= a2[v2]
            if v1 <= 0:
                return v2 + 1
        return -1
