class C1(object):

    def searchMatrix(self, a1, a2):
        """
        """
        if not a1:
            return False
        v1, v2 = (len(a1), len(a1[0]))
        v3, v4 = (0, v1 * v2)
        while v3 < v4:
            v5 = v3 + (v4 - v3) / 2
            if a1[v5 / v2][v5 % v2] >= a2:
                v4 = v5
            else:
                v3 = v5 + 1
        return v3 < v1 * v2 and a1[v3 / v2][v3 % v2] == a2
