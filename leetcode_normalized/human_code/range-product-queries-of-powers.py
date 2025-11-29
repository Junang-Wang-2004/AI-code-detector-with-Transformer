class C1(object):

    def productQueries(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0]
        v3 = 0
        while 1 << v3 <= a1:
            if a1 & 1 << v3:
                v2.append(v2[-1] + v3)
            v3 += 1
        return [pow(2, v2[r + 1] - v2[l], v1) for v4, v5 in a2]
