class C1(object):

    def minimumSum(self, a1):
        """
        """

        def binary_search(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1

        def binary_search_right(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if not a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a2

        def minimumArea(a1, a2, a3, a4):

            def count(a1, a2, a3, a4):
                v1 = a1[a3][a4]
                if a1 - 1 >= 0:
                    v1 -= a1[a1 - 1][a4]
                if a2 - 1 >= 0:
                    v1 -= a1[a3][a2 - 1]
                if a1 - 1 >= 0 and a2 - 1 >= 0:
                    v1 += a1[a1 - 1][a2 - 1]
                return v1
            v1 = binary_search(a1, a2, lambda i: count(a1, a3, i, a4))
            v2 = binary_search_right(a1, a2, lambda i: count(i, a3, a2, a4))
            v3 = binary_search(a3, a4, lambda j: count(a1, a3, a2, j))
            v4 = binary_search_right(a3, a4, lambda j: count(a1, j, a2, a4))
            return (v2 - v1 + 1) * (v4 - v3 + 1) if v1 <= a2 else 0
        for v1 in range(len(a1)):
            for v2 in range(len(a1[0])):
                if v1 - 1 >= 0:
                    a1[v1][v2] += a1[v1 - 1][v2]
                if v2 - 1 >= 0:
                    a1[v1][v2] += a1[v1][v2 - 1]
                if v1 - 1 >= 0 and v2 - 1 >= 0:
                    a1[v1][v2] -= a1[v1 - 1][v2 - 1]
        v3 = float('inf')
        v3 = float('inf')
        for v1 in range(len(a1) - 1):
            v4 = minimumArea(v1 + 1, len(a1) - 1, 0, len(a1[0]) - 1)
            for v2 in range(len(a1[0]) - 1):
                v5 = minimumArea(0, v1, 0, v2)
                v6 = minimumArea(0, v1, v2 + 1, len(a1[0]) - 1)
                v3 = min(v3, v4 + v5 + v6)
        for v1 in range(len(a1) - 1):
            v4 = minimumArea(0, v1, 0, len(a1[0]) - 1)
            for v2 in range(len(a1[0]) - 1):
                v5 = minimumArea(v1 + 1, len(a1) - 1, 0, v2)
                v6 = minimumArea(v1 + 1, len(a1) - 1, v2 + 1, len(a1[0]) - 1)
                v3 = min(v3, v4 + v5 + v6)
        for v2 in range(len(a1[0]) - 1):
            v4 = minimumArea(0, len(a1) - 1, v2 + 1, len(a1[0]) - 1)
            for v1 in range(len(a1) - 1):
                v5 = minimumArea(0, v1, 0, v2)
                v6 = minimumArea(v1 + 1, len(a1) - 1, 0, v2)
                v3 = min(v3, v4 + v5 + v6)
        for v2 in range(len(a1[0]) - 1):
            v4 = minimumArea(0, len(a1) - 1, 0, v2)
            for v1 in range(len(a1) - 1):
                v5 = minimumArea(0, v1, v2 + 1, len(a1[0]) - 1)
                v6 = minimumArea(v1 + 1, len(a1) - 1, v2 + 1, len(a1[0]) - 1)
                v3 = min(v3, v4 + v5 + v6)
        for v1 in range(len(a1) - 2):
            v4 = minimumArea(0, v1, 0, len(a1[0]) - 1)
            for v2 in range(v1 + 1, len(a1) - 1):
                v5 = minimumArea(v1 + 1, v2, 0, len(a1[0]) - 1)
                v6 = minimumArea(v2 + 1, len(a1) - 1, 0, len(a1[0]) - 1)
                v3 = min(v3, v4 + v5 + v6)
        for v1 in range(len(a1[0]) - 2):
            v4 = minimumArea(0, len(a1) - 1, 0, v1)
            for v2 in range(v1 + 1, len(a1[0]) - 1):
                v5 = minimumArea(0, len(a1) - 1, v1 + 1, v2)
                v6 = minimumArea(0, len(a1) - 1, v2 + 1, len(a1[0]) - 1)
                v3 = min(v3, v4 + v5 + v6)
        return v3
