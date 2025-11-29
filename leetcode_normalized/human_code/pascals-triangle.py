class C1(object):

    def generate(self, a1):
        v1 = []
        for v2 in range(a1):
            v1.append([])
            for v3 in range(v2 + 1):
                if v3 in (0, v2):
                    v1[v2].append(1)
                else:
                    v1[v2].append(v1[v2 - 1][v3 - 1] + v1[v2 - 1][v3])
        return v1

    def generate2(self, a1):
        if not a1:
            return []
        v1 = [[1]]
        for v2 in range(1, a1):
            v1 += [list(map(lambda x, y: x + y, v1[-1] + [0], [0] + v1[-1]))]
        return v1[:a1]

    def generate3(self, a1):
        """
        """
        if a1 == 0:
            return []
        if a1 == 1:
            return [[1]]
        v1 = [[1], [1, 1]]

        def add(a1):
            v1 = a1[:1]
            for v2, v3 in enumerate(a1):
                if v2 < len(a1) - 1:
                    v1 += [a1[v2] + a1[v2 + 1]]
            v1 += a1[:1]
            return v1
        while len(v1) < a1:
            v1.extend([add(v1[-1])])
        return v1
