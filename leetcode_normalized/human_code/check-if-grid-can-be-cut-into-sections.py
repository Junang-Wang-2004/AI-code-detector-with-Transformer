class C1(object):

    def checkValidCuts(self, a1, a2):
        """
        """

        def check(a1):
            v1 = 0
            v2 = a2[0][a1 + 2]
            for v3 in a2:
                v1 += int(v2 <= v3[a1])
                v2 = max(v2, v3[a1 + 2])
            return v1 >= 2
        for v1 in range(2):
            a2.sort(key=lambda x: x[v1])
            if check(v1):
                return True
        return False
