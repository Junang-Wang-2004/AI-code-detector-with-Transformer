class C1(object):

    def validMountainArray(self, a1):
        """
        """
        v1 = 0
        while v1 + 1 < len(a1) and a1[v1] < a1[v1 + 1]:
            v1 += 1
        v2 = len(a1) - 1
        while v2 - 1 >= 0 and a1[v2 - 1] > a1[v2]:
            v2 -= 1
        return 0 < v1 == v2 < len(a1) - 1
