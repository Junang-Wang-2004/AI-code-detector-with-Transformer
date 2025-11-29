class C1(object):

    def validPath(self, a1, a2, a3, a4):
        """
        """

        def dfs(a1, a2, a3):
            v1 = [a2]
            v2 = set(v1)
            while v1:
                v3 = v1.pop()
                if v3 == a3:
                    return True
                for v4 in reversed(a1[v3]):
                    if v4 in v2:
                        continue
                    v2.add(v4)
                    v1.append(v4)
            return False
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        return dfs(v1, a3, a4)
