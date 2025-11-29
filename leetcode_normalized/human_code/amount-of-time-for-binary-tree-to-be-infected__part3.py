class C1(object):

    def amountOfTime(self, a1, a2):
        """
        """

        def bfs(a1):
            v1 = collections.defaultdict(list)
            v2 = [a1]
            while v2:
                v3 = []
                for v4 in v2:
                    for v5 in (v4.left, v4.right):
                        if v5 is None:
                            continue
                        v1[v4.val].append(v5.val)
                        v1[v5.val].append(v4.val)
                        v3.append(v5)
                v2 = v3
            return v1

        def bfs2(a1, a2):
            v1 = -1
            v2 = [a2]
            v3 = {a2}
            while v2:
                v4 = []
                for v5 in v2:
                    for v6 in a1[v5]:
                        if v6 in v3:
                            continue
                        v3.add(v6)
                        v4.append(v6)
                v2 = v4
                v1 += 1
            return v1
        v1 = bfs(a1)
        return bfs2(v1, a2)
