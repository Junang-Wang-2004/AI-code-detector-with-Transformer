class C1(object):

    def sortArrayByParityII(self, a1):
        """
        """
        v1 = 1
        for v2 in range(0, len(a1), 2):
            if a1[v2] % 2:
                while a1[v1] % 2:
                    v1 += 2
                a1[v2], a1[v1] = (a1[v1], a1[v2])
        return a1
