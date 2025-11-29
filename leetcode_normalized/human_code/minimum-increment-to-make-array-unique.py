class C1(object):

    def minIncrementForUnique(self, a1):
        """
        """
        a1.sort()
        a1.append(float('inf'))
        v1, v2 = (0, 0)
        for v3 in range(1, len(a1)):
            if a1[v3 - 1] == a1[v3]:
                v2 += 1
                v1 -= a1[v3]
            else:
                v4 = min(v2, a1[v3] - a1[v3 - 1] - 1)
                v2 -= v4
                v1 += v4 * a1[v3 - 1] + v4 * (v4 + 1) // 2
        return v1
