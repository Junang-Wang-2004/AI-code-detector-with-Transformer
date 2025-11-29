import itertools

class C1(object):

    def maxTrailingZeros(self, a1):
        """
        """

        def factor(a1):
            v1 = [0] * 2
            for v2, v3 in enumerate([2, 5]):
                while a1 and a1 % v3 == 0:
                    a1 //= v3
                    v1[v2] += 1
            return v1

        def add(a1, a2):
            return [x + y for v1, v2 in zip(a1, a2)]

        def sub(a1, a2):
            return [x - y for v1, v2 in zip(a1, a2)]
        v1 = [[None for v2 in range(len(a1[0]))] for v2 in range(len(a1))]
        for v3 in range(len(a1)):
            v1[v3][0] = factor(a1[v3][0])
            for v4 in range(1, len(a1[0])):
                v1[v3][v4] = add(v1[v3][v4 - 1], factor(a1[v3][v4]))
        v5 = 0
        for v4 in range(len(a1[0])):
            v6 = [0] * 2
            for v3 in range(len(a1)):
                v6 = add(v6, factor(a1[v3][v4]))
            v7 = [0] * 2
            for v3 in range(len(a1)):
                v8 = sub(v1[v3][-1], v1[v3][v4 - 1] if v4 else [0] * 2)
                v5 = max(v5, min(add(v1[v3][v4], v7)), min(add(v8, v7)))
                v7 = add(v7, factor(a1[v3][v4]))
                v9 = sub(v6, v7)
                v5 = max(v5, min(add(v1[v3][v4], v9)), min(add(v8, v9)))
        return v5
