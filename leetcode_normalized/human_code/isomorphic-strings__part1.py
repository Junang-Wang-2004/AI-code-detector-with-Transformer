class C1(object):

    def isIsomorphic(self, a1, a2):
        """
        """
        if len(a1) != len(a2):
            return False
        v1, v2 = ({}, {})
        for v3, v4 in zip(a1, a2):
            if v4 not in v1 and v3 not in v2:
                v1[v4] = v3
                v2[v3] = v4
            elif v4 not in v1 or v1[v4] != v3:
                return False
        return True
