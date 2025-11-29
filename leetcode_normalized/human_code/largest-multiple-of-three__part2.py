class C1(object):

    def largestMultipleOfThree(self, a1):
        """
        """

        def candidates_gen(a1):
            if a1 == 0:
                return
            for v1 in range(10):
                yield [v1]
            for v1 in range(10):
                for v2 in range(v1 + 1):
                    yield [v1, v2]
        v1, v2 = (collections.Counter(a1), sum(a1) % 3)
        for v3 in candidates_gen(v2):
            v4 = collections.Counter(v3)
            if sum(v3) % 3 == v2 and all((v1[k] >= v for v5, v6 in v4.items())):
                for v5, v6 in v4.items():
                    v1[v5] -= v6
                break
        v7 = ''.join((str(d) * v1[d] for v8 in reversed(range(10))))
        return '0' if v7 and v7[0] == '0' else v7
