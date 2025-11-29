class C1(object):

    def searchMatrix(self, a1, a2):
        v1 = len(a1)
        if v1 == 0:
            return False
        v2 = len(a1[0])
        if v2 == 0:
            return False
        v3, v4 = (0, v2 - 1)
        while v3 < v1 and v4 >= 0:
            if a1[v3][v4] == a2:
                return True
            elif a1[v3][v4] > a2:
                v4 -= 1
            else:
                v3 += 1
        return False
