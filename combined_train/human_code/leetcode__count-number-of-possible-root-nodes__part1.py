import collections

class C1(object):

    def rootCount(self, a1, a2, a3):
        """
        """

        def iter_dfs():
            v1 = 0
            v2 = [(0, -1)]
            while v2:
                v3, v4 = v2.pop()
                v1 += int((v4, v3) in lookup)
                for v5 in adj[v3]:
                    if v5 == v4:
                        continue
                    v2.append((v5, v3))
            return v1

        def iter_dfs2(a1):
            v1 = 0
            v2 = [(0, -1, a1)]
            while v2:
                v3, v4, a1 = v2.pop()
                if (v4, v3) in lookup:
                    a1 -= 1
                if (v3, v4) in lookup:
                    a1 += 1
                v1 += int(a1 >= a3)
                for v6 in adj[v3]:
                    if v6 == v4:
                        continue
                    v2.append((v6, v3, a1))
            return v1
        v1 = collections.defaultdict(list)
        for v2, v3 in a1:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = {(v2, v3) for v2, v3 in a2}
        v5 = iter_dfs()
        return iter_dfs2(v5)
