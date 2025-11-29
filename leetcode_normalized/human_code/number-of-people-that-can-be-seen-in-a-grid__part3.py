class C1(object):

    def seePeople(self, a1):
        """
        """

        def count(a1, a2, a3, a4):
            while a3 and a1(a3[-1]) < a1(a2):
                increase(a3.pop())
            if a3:
                increase(a3[-1])
            if a3 and a1(a3[-1]) == a1(a2):
                a3.pop()
            a3.append(a2)
        v1 = [[0] * len(a1[0]) for v2 in range(len(a1))]
        for v3 in range(len(a1)):
            v4 = []

            def increase(a1):
                v1[v3][a1] += 1
            for v5 in range(len(a1[0])):
                count(lambda x: a1[v3][x], v5, v4, add)
        for v5 in range(len(a1[0])):
            v4 = []

            def increase(a1):
                v1[a1][v5] += 1
            for v3 in range(len(a1)):
                count(lambda x: a1[x][v5], v3, v4, add)
        return v1
