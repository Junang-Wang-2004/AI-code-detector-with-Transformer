import collections

class C1(object):

    def goodSubtreeSum(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7

        def get_mask(a1):
            v1 = 0
            while a1:
                a1, v3 = divmod(a1, 10)
                if v1 & 1 << v3:
                    return -1
                v1 |= 1 << v3
            return v1

        def dfs(a1):
            v1 = collections.defaultdict(int)
            v1[0] = 0
            v2 = get_mask(a1[a1])
            if v2 != -1:
                v1[v2] = a1[a1]
            for v3 in adj[a1]:
                v4 = dfs(v3)
                for v5, v6 in list(v1.items()):
                    for v7, v8 in v4.items():
                        if v5 & v7:
                            continue
                        v1[v5 | v7] = max(v1[v5 | v7], v6 + v8)
            result[0] = (result[0] + max(v1.values())) % v1
            return v1
        v2 = [[] for v3 in range(len(a1))]
        for v4 in range(1, len(a2)):
            v2[a2[v4]].append(v4)
        v5 = [0]
        dfs(0)
        return v5[0]
