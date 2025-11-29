class C1(object):

    def wordPattern(self, a1, a2):
        """
        """
        v1 = a2.split()
        if len(a1) != len(v1):
            return False
        v2, v3 = ({}, {})
        for v4, v5 in zip(a1, v1):
            if v5 not in v2 and v4 not in v3:
                v2[v5] = v4
                v3[v4] = v5
            elif v5 not in v2 or v2[v5] != v4:
                return False
        return True
