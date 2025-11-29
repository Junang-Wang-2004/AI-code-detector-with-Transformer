class C1(object):

    def isPossible(self, a1):
        """
        """
        v1, v2 = (float('-inf'), 0)
        v3, v4, v5 = (0, 0, 0)
        v6 = 0
        while v6 < len(a1):
            v7 = 0
            v2 = a1[v6]
            while v6 < len(a1) and v2 == a1[v6]:
                v7 += 1
                v6 += 1
            if v2 != v1 + 1:
                if v3 != 0 or v4 != 0:
                    return False
                v3, v4, v5 = (v7, 0, 0)
            else:
                if v7 < v3 + v4:
                    return False
                v3, v4, v5 = (max(0, v7 - (v3 + v4 + v5)), v3, v4 + min(v5, v7 - (v3 + v4)))
            v1 = v2
        return v3 == 0 and v4 == 0
