class C1(object):

    def findErrorNums(self, a1):
        """
        """
        v1 = [0] * 2
        for v2 in a1:
            if a1[abs(v2) - 1] < 0:
                v1[0] = abs(v2)
            else:
                a1[abs(v2) - 1] *= -1
        for v2 in range(len(a1)):
            if a1[v2] > 0:
                v1[1] = v2 + 1
            else:
                a1[v2] *= -1
        return v1
