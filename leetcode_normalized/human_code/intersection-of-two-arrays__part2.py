class C1(object):

    def intersection(self, a1, a2):
        """
        """
        if len(a1) > len(a2):
            return self.intersection(a2, a1)

        def binary_search(a1, a2, a3, a4, a5):
            while a3 < a4:
                v1 = a3 + (a4 - a3) / 2
                if a1(a2[v1], a5):
                    a4 = v1
                else:
                    a3 = v1 + 1
            return a3
        (a1.sort(), a2.sort())
        v1 = []
        v2 = 0
        for v3 in a1:
            v2 = binary_search(lambda x, y: x >= y, a2, v2, len(a2), v3)
            if v2 != len(a2) and a2[v2] == v3:
                v1 += (v3,)
                v2 = binary_search(lambda x, y: x > y, a2, v2, len(a2), v3)
        return v1
