class C1(object):

    def findColumnWidth(self, a1):
        """
        """

        def length(a1):
            v1 = 1
            if a1 < 0:
                a1 = -a1
                v1 += 1
            while a1 >= 10:
                a1 //= 10
                v1 += 1
            return v1
        return [max((length(a1[i][j]) for v1 in range(len(a1)))) for v2 in range(len(a1[0]))]
