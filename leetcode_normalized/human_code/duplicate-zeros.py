class C1(object):

    def duplicateZeros(self, a1):
        """
        """
        v1, v2 = (0, 0)
        while v2 + v1 < len(a1):
            v1 += int(a1[v2] == 0)
            v2 += 1
        v2 -= 1
        while v1:
            if v2 + v1 < len(a1):
                a1[v2 + v1] = a1[v2]
            if a1[v2] == 0:
                v1 -= 1
                a1[v2 + v1] = a1[v2]
            v2 -= 1
