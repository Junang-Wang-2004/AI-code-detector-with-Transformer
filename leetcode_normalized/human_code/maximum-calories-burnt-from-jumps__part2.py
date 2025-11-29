class C1(object):

    def maxCaloriesBurnt(self, a1):
        """
        """
        a1.sort()
        v1 = 0
        v2, v3 = (0, len(a1) - 1)
        v4 = (0 - a1[v3]) ** 2
        while v2 != v3:
            v4 += (a1[v3] - a1[v2]) ** 2
            v2 += v1
            v1 ^= 1
            v3 -= v1
        return v4
