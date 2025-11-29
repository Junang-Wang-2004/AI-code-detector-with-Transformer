class C1(object):

    def constructArray(self, a1, a2):
        """
        """
        v1 = []
        v2, v3 = (1, a1)
        while v2 <= v3:
            if a2 % 2:
                v1.append(v2)
                v2 += 1
            else:
                v1.append(v3)
                v3 -= 1
            if a2 > 1:
                a2 -= 1
        return v1
