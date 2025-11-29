class C1(object):

    def tilingRectangle(self, a1, a2):
        """
        """

        def find_next(a1):
            for v1 in range(len(a1)):
                for v2 in range(len(a1[0])):
                    if not a1[v1][v2]:
                        return (v1, v2)
            return (-1, -1)

        def find_max_length(a1, a2, a3):
            v1 = 1
            while a2 + v1 - 1 < len(a1) and a3 + v1 - 1 < len(a1[0]):
                for v2 in range(a2, a2 + v1 - 1):
                    if a1[v2][a3 + v1 - 1]:
                        return v1 - 1
                for v3 in range(a3, a3 + v1):
                    if a1[a2 + v1 - 1][v3]:
                        return v1 - 1
                v1 += 1
            return v1 - 1

        def fill(a1, a2, a3, a4, a5):
            for v1 in range(a2, a2 + a4):
                for v2 in range(a3, a3 + a4):
                    a1[v1][v2] = a5

        def backtracking(a1, a2, a3):
            if a2 >= a3[0]:
                return
            v1, v2 = find_next(a1)
            if (v1, v2) == (-1, -1):
                a3[0] = min(a3[0], a2)
                return
            v3 = find_max_length(a1, v1, v2)
            for v4 in reversed(range(1, v3 + 1)):
                fill(a1, v1, v2, v4, 1)
                backtracking(a1, a2 + 1, a3)
                fill(a1, v1, v2, v4, 0)
        if a2 > a1:
            return self.tilingRectangle(a2, a1)
        v1 = [[0] * a2 for v2 in range(a1)]
        v3 = [float('inf')]
        backtracking(v1, 0, v3)
        return v3[0]
