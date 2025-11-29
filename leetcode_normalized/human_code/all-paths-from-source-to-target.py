class C1(object):

    def allPathsSourceTarget(self, a1):
        """
        """

        def dfs(a1, a2, a3, a4):
            if a2 == len(a1) - 1:
                a4.append(a3[:])
                return
            for v1 in a1[a2]:
                a3.append(v1)
                dfs(a1, v1, a3, a4)
                a3.pop()
        v1 = []
        dfs(a1, 0, [0], v1)
        return v1
