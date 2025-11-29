class C1(object):

    def restoreString(self, a1, a2):
        """
        """
        v1 = list(a1)
        for v2, v3 in enumerate(v1):
            if a2[v2] == v2:
                continue
            v4, v5 = (v3, a2[v2])
            while v5 != v2:
                v1[v5], v4 = (v4, v1[v5])
                a2[v5], v5 = (v5, a2[v5])
            v1[v2] = v4
        return ''.join(v1)
