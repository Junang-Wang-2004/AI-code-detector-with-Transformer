class C1(object):

    def maxCaloriesBurnt(self, a1):
        """
        """
        a1.sort()
        v1, v2 = (0, len(a1) - 1)
        v3 = (0 - a1[v2]) ** 2
        while v1 != v2:
            v3 += (a1[v2] - a1[v1]) ** 2
            v2 -= 1
            if v1 == v2:
                break
            v3 += (a1[v1] - a1[v2]) ** 2
            v1 += 1
        return v3
