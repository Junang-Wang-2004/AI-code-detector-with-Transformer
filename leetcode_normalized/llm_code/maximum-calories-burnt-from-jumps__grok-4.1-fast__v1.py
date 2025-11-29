class C1(object):

    def maxCaloriesBurnt(self, a1):
        v1 = sorted(a1)
        v2 = 0
        v3 = len(v1) - 1
        v4 = v1[v3] * v1[v3]
        while v2 < v3:
            v4 += (v1[v3] - v1[v2]) * (v1[v3] - v1[v2])
            v3 -= 1
            if v2 < v3:
                v4 += (v1[v2] - v1[v3]) * (v1[v2] - v1[v3])
                v2 += 1
        return v4
