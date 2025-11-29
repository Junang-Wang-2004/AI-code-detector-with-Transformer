import collections

class C1(object):

    def differByOne(self, a1):
        """
        """
        v1, v2 = (10 ** 9 + 7, 113)
        v3 = [0] * len(a1)
        for v4, v5 in enumerate(a1):
            for v6 in v5:
                v3[v4] = (v2 * v3[v4] + (ord(v6) - ord('a'))) % v1
        v7 = 1
        for v8 in reversed(range(len(a1[0]))):
            v9 = collections.defaultdict(list)
            for v4, v5 in enumerate(a1):
                v10 = (v3[v4] - v7 * (ord(v5[v8]) - ord('a'))) % v1
                if v10 in v9:
                    for v11 in v9[v10]:
                        if a1[v11][:v8] + a1[v11][v8 + 1:] == v5[:v8] + v5[v8 + 1:]:
                            return True
                v9[v10].append(v4)
            v7 = v2 * v7 % v1
        return False
