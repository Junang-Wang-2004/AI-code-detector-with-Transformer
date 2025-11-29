class C1(object):

    def distributeCandies(self, a1, a2):
        """
        """
        v1 = [0] * a2
        v2 = 0
        while a1 != 0:
            v1[v2 % a2] += min(a1, v2 + 1)
            a1 -= min(a1, v2 + 1)
            v2 += 1
        return v1
