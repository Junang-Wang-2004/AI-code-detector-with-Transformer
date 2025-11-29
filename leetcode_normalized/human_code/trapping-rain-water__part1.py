class C1(object):

    def trap(self, a1):
        """
        """
        v1, v2, v3, v4 = (0, 0, len(a1) - 1, 0)
        while v2 < v3:
            if a1[v2] < a1[v3]:
                v5 = a1[v2]
                v2 += 1
            else:
                v5 = a1[v3]
                v3 -= 1
            v4 = max(v4, v5)
            v1 += v4 - v5
        return v1
