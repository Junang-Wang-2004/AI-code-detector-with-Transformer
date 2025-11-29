import collections

class C1(object):

    def validPath(self, a1, a2, a3, a4):
        """
        """

        def bi_bfs(a1, a2, a3):
            v1, v2 = ({a2}, {a3})
            v3 = set()
            v4 = 0
            while v1:
                for v5 in v1:
                    v3.add(v5)
                v6 = set()
                for v5 in v1:
                    if v5 in v2:
                        return v4
                    for v7 in a1[v5]:
                        if v7 in v3:
                            continue
                        v6.add(v7)
                v1 = v6
                v4 += 1
                if len(v1) > len(v2):
                    v1, v2 = (v2, v1)
            return -1
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        return bi_bfs(v1, a3, a4) >= 0
