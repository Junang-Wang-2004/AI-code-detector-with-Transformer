import collections

class C1(object):

    def countBlackBlocks(self, a1, a2, a3):
        """
        """
        v1 = 2
        v2 = collections.Counter()
        for v3, v4 in a3:
            for v5 in range(max(v3 - (v1 - 1), 0), min(v3 + 1, a1 - (v1 - 1))):
                for v6 in range(max(v4 - (v1 - 1), 0), min(v4 + 1, a2 - (v1 - 1))):
                    v2[v5, v6] += 1
        v7 = [0] * (v1 ** 2 + 1)
        for v8 in v2.values():
            v7[v8] += 1
        v7[0] = (a1 - (v1 - 1)) * (a2 - (v1 - 1)) - sum((v7[i] for v9 in range(1, len(v7))))
        return v7
