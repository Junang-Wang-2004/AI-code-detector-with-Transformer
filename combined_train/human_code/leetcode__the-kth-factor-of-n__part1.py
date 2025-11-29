class C1(object):

    def kthFactor(self, a1, a2):
        """
        """

        def kth_factor(a1, a2=0):
            v1 = None
            v2 = 1
            while v2 * v2 <= a1:
                if not a1 % v2:
                    v1 = v2
                    a2 -= 1
                    if not a2:
                        break
                v2 += 1
            return (v1, -a2)
        v1, v2 = kth_factor(a1)
        v3 = 2 * v2 - (v1 * v1 == a1)
        if a2 > v3:
            return -1
        v4 = kth_factor(a1, a2 if a2 <= v2 else v3 - (a2 - 1))[0]
        return v4 if a2 <= v2 else a1 // v4
