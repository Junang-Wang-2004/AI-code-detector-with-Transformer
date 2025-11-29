class C1(object):

    def countArrangement(self, a1):
        """
        """

        def countArrangementHelper(a1, a2):
            if a1 <= 0:
                return 1
            v1 = 0
            for v2 in range(a1):
                if a2[v2] % a1 == 0 or a1 % a2[v2] == 0:
                    a2[v2], a2[a1 - 1] = (a2[a1 - 1], a2[v2])
                    v1 += countArrangementHelper(a1 - 1, a2)
                    a2[v2], a2[a1 - 1] = (a2[a1 - 1], a2[v2])
            return v1
        return countArrangementHelper(a1, list(range(1, a1 + 1)))
