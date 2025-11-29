class C1(object):

    def cycleLengthQueries(self, a1, a2):
        """
        """
        v1 = []
        for v2, v3 in a2:
            v4 = 1
            while v2 != v3:
                if v2 > v3:
                    v2, v3 = (v3, v2)
                v3 //= 2
                v4 += 1
            v1.append(v4)
        return v1
