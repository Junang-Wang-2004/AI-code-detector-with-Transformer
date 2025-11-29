class C1:

    def searchMatrix(self, a1, a2):
        if not a1 or not a1[0]:
            return False
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = 0
        v4 = v2 - 1
        while v3 < v1 and v4 >= 0:
            v5 = a1[v3][v4]
            if v5 == a2:
                return True
            elif v5 > a2:
                v4 -= 1
            else:
                v3 += 1
        return False
