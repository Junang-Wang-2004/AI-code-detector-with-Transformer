class C1(object):

    def reverseString(self, a1):
        """
        """
        v1, v2 = (0, len(a1) - 1)
        while v1 < v2:
            a1[v1], a1[v2] = (a1[v2], a1[v1])
            v1 += 1
            v2 -= 1
