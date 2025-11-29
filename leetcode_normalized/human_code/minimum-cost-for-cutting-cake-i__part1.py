class C1(object):

    def minimumCost(self, a1, a2, a3, a4):
        """
        """
        a3.sort()
        a4.sort()
        v1 = 0
        v2 = v3 = 1
        while a3 or a4:
            if not a4 or (a3 and a3[-1] > a4[-1]):
                v1 += a3.pop() * v2
                v3 += 1
            else:
                v1 += a4.pop() * v3
                v2 += 1
        return v1
