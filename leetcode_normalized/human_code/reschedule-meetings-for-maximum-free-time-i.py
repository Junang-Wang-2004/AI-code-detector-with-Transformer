class C1(object):

    def maxFreeTime(self, a1, a2, a3, a4):
        """
        """
        a3.append(a1)
        a4.insert(0, 0)
        v1 = v2 = 0
        for v3 in range(len(a3)):
            v2 += a3[v3] - a4[v3]
            v1 = max(v1, v2)
            if v3 - a2 >= 0:
                v2 -= a3[v3 - a2] - a4[v3 - a2]
        return v1
