import collections

class C1(object):

    def minTransfers(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        for v2, v3, v4 in a1:
            v1[v2] += v4
            v1[v3] -= v4
        v5 = [account for v6 in v1.values() if v6]
        v7 = [0] * 2 ** len(v5)
        v8 = [0] * 2 ** len(v5)
        for v9 in range(len(v7)):
            v10 = 1
            for v11 in range(len(v5)):
                if v9 & v10 == 0:
                    v12 = v9 | v10
                    v8[v12] = v8[v9] + v5[v11]
                    if v8[v12] == 0:
                        v7[v12] = max(v7[v12], v7[v9] + 1)
                    else:
                        v7[v12] = max(v7[v12], v7[v9])
                v10 <<= 1
        return len(v5) - v7[-1]
