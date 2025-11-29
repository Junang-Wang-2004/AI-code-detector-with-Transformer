import itertools

class C1(object):

    def minimumCost(self, a1, a2, a3):
        """
        """
        v1 = float('inf')

        def query(a1):
            v1 = trie
            for v2 in range(a1, len(a1)):
                v3 = a1[v2]
                if v3 not in v1:
                    break
                v1 = v1[v3]
                if '_end' in v1:
                    dp[v2 + 1] = min(dp[v2 + 1], dp[a1] + v1['_end'])
        v2 = lambda: collections.defaultdict(v2)
        v3 = v2()
        for v4, v5 in zip(a2, a3):
            v6 = reduce(dict.__getitem__, v4, v3)
            if '_end' not in v6:
                v6['_end'] = v1
            v6['_end'] = min(v6['_end'], v5)
        v7 = [v1] * (len(a1) + 1)
        v7[0] = 0
        for v8 in range(len(a1)):
            if v7[v8] == v1:
                continue
            query(v8)
        return v7[-1] if v7[-1] != v1 else -1
