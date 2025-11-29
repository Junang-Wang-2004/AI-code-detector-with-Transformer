class C1(object):

    def modifiedMatrix(self, a1):
        """
        """
        for v1 in range(len(a1[0])):
            v2 = max((a1[i][v1] for v3 in range(len(a1))))
            for v3 in range(len(a1)):
                if a1[v3][v1] == -1:
                    a1[v3][v1] = v2
        return a1
