class C1(object):

    def isTrionic(self, a1):
        """
        """
        v1 = 0
        while v1 + 1 < len(a1) and a1[v1] < a1[v1 + 1]:
            v1 += 1
        v2 = v1
        while v2 + 1 < len(a1) and a1[v2] > a1[v2 + 1]:
            v2 += 1
        v3 = v2
        while v3 + 1 < len(a1) and a1[v3] < a1[v3 + 1]:
            v3 += 1
        return 0 < v1 < v2 < v3 == len(a1) - 1
