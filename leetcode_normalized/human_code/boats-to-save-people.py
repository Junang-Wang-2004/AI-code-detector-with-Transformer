class C1(object):

    def numRescueBoats(self, a1, a2):
        """
        """
        a1.sort()
        v1 = 0
        v2, v3 = (0, len(a1) - 1)
        while v2 <= v3:
            v1 += 1
            if a1[v2] + a1[v3] <= a2:
                v2 += 1
            v3 -= 1
        return v1
