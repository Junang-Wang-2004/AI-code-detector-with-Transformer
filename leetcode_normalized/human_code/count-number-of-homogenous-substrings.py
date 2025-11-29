class C1(object):

    def countHomogenous(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = v3 = 0
        for v4 in range(len(a1)):
            if v4 and a1[v4 - 1] == a1[v4]:
                v3 += 1
            else:
                v3 = 1
            v2 = (v2 + v3) % v1
        return v2
