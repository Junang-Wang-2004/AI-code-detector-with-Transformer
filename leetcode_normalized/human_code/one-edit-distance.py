class C1(object):

    def isOneEditDistance(self, a1, a2):
        """
        """
        v1, v2 = (len(a1), len(a2))
        if v1 > v2:
            return self.isOneEditDistance(a2, a1)
        if v2 - v1 > 1:
            return False
        v3, v4 = (0, v2 - v1)
        while v3 < v1 and a1[v3] == a2[v3]:
            v3 += 1
        if v4 == 0:
            v3 += 1
        while v3 < v1 and a1[v3] == a2[v3 + v4]:
            v3 += 1
        return v3 == v1
