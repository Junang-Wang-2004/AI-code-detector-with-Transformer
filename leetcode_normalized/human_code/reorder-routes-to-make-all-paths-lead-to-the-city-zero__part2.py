import collections

class C1(object):

    def minReorder(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3, a4, a5):
            v1 = a4 * a1 + a5 in a2
            for v2 in a3[a5]:
                if v2 == a4:
                    continue
                v1 += dfs(a1, a2, a3, a5, v2)
            return v1
        v1, v2 = (set(), collections.defaultdict(list))
        for v3, v4 in a2:
            v1.add(v3 * a1 + v4)
            v2[v4].append(v3)
            v2[v3].append(v4)
        return dfs(a1, v1, v2, -1, 0)
