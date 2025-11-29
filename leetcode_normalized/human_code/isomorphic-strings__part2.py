class C1(object):

    def isIsomorphic(self, a1, a2):
        if len(a1) != len(a2):
            return False
        return self.halfIsom(a1, a2) and self.halfIsom(a2, a1)

    def halfIsom(self, a1, a2):
        v1 = {}
        for v2 in range(len(a1)):
            if a1[v2] not in v1:
                v1[a1[v2]] = a2[v2]
            elif v1[a1[v2]] != a2[v2]:
                return False
        return True
