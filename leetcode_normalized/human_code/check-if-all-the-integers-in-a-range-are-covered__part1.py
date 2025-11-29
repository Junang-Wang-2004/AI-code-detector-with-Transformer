class C1(object):

    def isCovered(self, a1, a2, a3):
        """
        """
        v1 = 50
        v2 = [0] * (v1 + 1)
        for v3, v4 in a1:
            v2[v3 - 1] += 1
            v2[v4 - 1 + 1] -= 1
        v5 = 0
        for v6 in range(a3 - 1 + 1):
            v5 += v2[v6]
            if v6 >= a2 - 1 and (not v5):
                return False
        return True
