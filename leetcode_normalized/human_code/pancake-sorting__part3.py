class C1(object):

    def pancakeSort(self, a1):
        """
        """

        def reverse(a1, a2, a3):
            for v1 in range((a3 - a2) // 2):
                a1[a2 + v1], a1[a3 - 1 - v1] = (a1[a3 - 1 - v1], a1[a2 + v1])
        v1 = []
        for v2 in reversed(range(1, len(a1) + 1)):
            v3 = a1.index(v2)
            reverse(a1, 0, v3 + 1)
            v1.append(v3 + 1)
            reverse(a1, 0, v2)
            v1.append(v2)
        return v1
