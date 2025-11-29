class C1(object):

    def sumOfPower(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * (a2 + 1)
        v2[0] = 1
        for v3 in a1:
            for v4 in reversed(range(a2 + 1)):
                v2[v4] = (v2[v4] + (v2[v4] + (v2[v4 - v3] if v4 - v3 >= 0 else 0))) % v1
        return v2[a2]
