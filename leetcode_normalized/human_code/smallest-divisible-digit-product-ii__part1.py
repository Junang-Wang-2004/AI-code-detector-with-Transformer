class C1(object):

    def smallestNumber(self, a1, a2):
        """
        """
        v1 = [[(0, 0, 0, 0), (0, 1, 0, 0)], [(1, 0, 0, 0), (0, 0, 0, 1)], [(0, 0, 1, 0), (1, 0, 0, 1)]]

        def count(a1):
            v1 = [0] * 10
            for v2 in range(2, 9 + 1):
                while a1 % v2 == 0:
                    a1 //= v2
                    v1[v2] += 1
                if a1 == 1:
                    return v1
            return []

        def update(a1, a2, a3):
            for v1, v2 in enumerate(a2):
                a1[v1] += a3 * v2

        def diff(a1, a2):
            return [max(a1[i] - a2[i], 0) for v1 in range(len(a1))]

        def min_factors(a1):
            v1, v2 = divmod(a1[2], 3)
            v3, v4 = divmod(a1[3], 2)
            v5, v6, v7, v8 = v1[v2][v4]
            return (v5, v6, v7, a1[5], v8, a1[7], v1, v3)

        def format(a1, a2):
            return '1' * (a2 - sum(a1)) + ''.join((str(x) * a1[x - 2] for v1 in range(2, 9 + 1)))
        v2 = count(a2)
        if not v2:
            return '-1'
        v3 = list(map(int, a1))
        v4 = next((v4 for v4 in range(len(v3)) if not v3[v4]), len(v3))
        for v5 in range(v4, len(v3)):
            v3[v5] = 1
        v6 = [0] * 10
        for v7 in v3:
            update(v6, count(v7), +1)
        if all((d == 0 for v8 in diff(v2, v6))):
            return ''.join(map(str, v3))
        for v4 in reversed(range(len(v3))):
            update(v6, count(v3[v4]), -1)
            for v7 in range(v3[v4] + 1, 9 + 1):
                update(v6, count(v7), +1)
                v9 = min_factors(diff(v2, v6))
                update(v6, count(v7), -1)
                if sum(v9) > len(v3) - 1 - v4:
                    continue
                return ''.join(map(str, v3[:v4])) + str(v7) + format(v9, len(v3) - 1 - v4)
        return format(min_factors(diff(v2, v6)), len(v3) + 1)
