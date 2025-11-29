class C1(object):

    def buildArray(self, a1):
        """
        """
        for v1 in range(len(a1)):
            v2, v3 = (v1, a1[v1])
            while v3 >= 0 and v3 != v1:
                a1[v2], a1[v3] = (~a1[v3], ~a1[v2] if v2 == v1 else a1[v2])
                v2, v3 = (v3, ~a1[v2])
        for v1 in range(len(a1)):
            if a1[v1] < 0:
                a1[v1] = ~a1[v1]
        return a1
