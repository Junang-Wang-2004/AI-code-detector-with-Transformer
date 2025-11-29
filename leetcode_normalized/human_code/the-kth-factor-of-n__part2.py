class C1(object):

    def kthFactor(self, a1, a2):
        """
        """
        v1 = []
        v2 = 1
        while v2 * v2 <= a1:
            if not a1 % v2:
                if v2 * v2 != a1:
                    v1.append(v2)
                a2 -= 1
                if not a2:
                    return v2
            v2 += 1
        return -1 if a2 > len(v1) else a1 // v1[-a2]
