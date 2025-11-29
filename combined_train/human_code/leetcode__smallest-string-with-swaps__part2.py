import itertools

class C1(object):

    def smallestStringWithSwaps(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3, a4):
            a3.add(a1)
            a4.append(a1)
            for v1 in a2[a1]:
                if v1 in a3:
                    continue
                dfs(v1, a2, a3, a4)
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = set()
        v5 = list(a1)
        for v2 in range(len(a1)):
            if v2 in v4:
                continue
            v6 = []
            dfs(v2, v1, v4, v6)
            v6.sort()
            v7 = sorted((v5[k] for v8 in v6))
            for v9, v10 in zip(v6, v7):
                v5[v9] = v10
        return ''.join(v5)
