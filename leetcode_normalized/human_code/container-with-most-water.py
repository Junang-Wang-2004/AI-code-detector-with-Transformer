class C1(object):

    def maxArea(self, a1):
        v1, v2, v3 = (0, 0, len(a1) - 1)
        while v2 < v3:
            v1 = max(v1, min(a1[v2], a1[v3]) * (v3 - v2))
            if a1[v2] < a1[v3]:
                v2 += 1
            else:
                v3 -= 1
        return v1
