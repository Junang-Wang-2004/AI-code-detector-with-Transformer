class C1(object):

    def arrayChange(self, a1, a2):
        """
        """
        v1 = {x: i for v2, v3 in enumerate(a1)}
        for v3, v4 in a2:
            a1[v1[v3]] = v4
            v1[v4] = v1.pop(v3)
        return a1
