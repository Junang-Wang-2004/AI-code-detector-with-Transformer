class C1(object):

    def prevPermOpt1(self, a1):
        """
        """
        for v1 in reversed(range(len(a1) - 1)):
            if a1[v1] > a1[v1 + 1]:
                break
        else:
            return a1
        v2 = len(a1) - 1
        while a1[v1] <= a1[v2]:
            v2 -= 1
        while a1[v2 - 1] == a1[v2]:
            v2 -= 1
        a1[v1], a1[v2] = (a1[v2], a1[v1])
        return a1
