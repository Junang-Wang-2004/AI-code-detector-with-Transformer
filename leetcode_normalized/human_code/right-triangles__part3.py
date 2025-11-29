class C1(object):

    def numberOfRightTriangles(self, a1):
        """
        """

        def get(a1, a2):
            return a1[a1][a2] if n < m else a1[a2][a1]

        def count(a1):
            v1 = 0
            v2 = [0] * min(n, m)
            for v3 in a1(range(max(n, m))):
                v4 = sum((get(i, v3) for v5 in range(len(v2))))
                for v5 in range(len(v2)):
                    if get(v5, v3) == 0:
                        continue
                    v1 += v2[v5]
                    v2[v5] += v4 - 1
            return v1
        v1, v2 = (len(a1), len(a1[0]))
        return count(lambda x: x) + count(reversed)
