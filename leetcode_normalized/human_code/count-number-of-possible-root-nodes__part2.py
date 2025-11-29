import collections

class C1(object):

    def rootCount(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2):
            v1 = int((a2, a1) in lookup)
            for v2 in adj[a1]:
                if v2 == a2:
                    continue
                v1 += dfs(v2, a1)
            return v1

        def dfs2(a1, a2, a3):
            if (a2, a1) in lookup:
                a3 -= 1
            if (a1, a2) in lookup:
                a3 += 1
            v2 = int(a3 >= a3)
            for v3 in adj[a1]:
                if v3 == a2:
                    continue
                v2 += dfs2(v3, a1, a3)
            return v2
        v1 = collections.defaultdict(list)
        for v2, v3 in a1:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = {(v2, v3) for v2, v3 in a2}
        v5 = dfs(0, -1)
        return dfs2(0, -1, v5)
