class C1(object):

    def queryConversions(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7

        def divmod(a1, a2):
            return a1 * pow(a2, v1 - 2, v1) % v1

        def unit():
            v1 = [[] for v2 in range(len(a1) + 1)]
            for v3, v4, v5 in a1:
                v1[v3].append((v4, v5))
            v6 = [0] * len(v1)
            v6[0] = 1
            v7 = [0]
            while v7:
                v8 = []
                for v3 in v7:
                    for v4, v5 in v1[v3]:
                        v6[v4] = v6[v3] * v5 % v1
                        v8.append(v4)
                v7 = v8
            return v6
        v2 = unit()
        return [divmod(v2[b], v2[a]) for v3, v4 in a2]
