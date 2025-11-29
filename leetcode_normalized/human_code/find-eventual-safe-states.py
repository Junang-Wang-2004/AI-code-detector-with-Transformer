class C1(object):

    def eventualSafeNodes(self, a1):
        """
        """
        v1, v2, v3 = list(range(3))

        def dfs(a1, a2, a3):
            if a3[a2] != v1:
                return a3[a2] == v3
            a3[a2] = v2
            if any((not dfs(a1, child, a3) for v1 in a1[a2])):
                return False
            a3[a2] = v3
            return True
        v4 = [v1] * len(a1)
        return [node for v5 in range(len(a1)) if dfs(a1, v5, v4)]
