class C1(object):

    def permute(self, a1):
        """
        """
        v1 = []
        self.dfs(a1, [], v1)
        return v1

    def dfs(self, a1, a2, a3):
        if not a1:
            a3.append(a2)
        for v1 in range(len(a1)):
            self.dfs(a1[:v1] + a1[v1 + 1:], a2 + [a1[v1]], a3)
