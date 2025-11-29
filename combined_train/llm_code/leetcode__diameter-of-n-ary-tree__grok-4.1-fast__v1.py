class C1:

    def diameter(self, a1):
        if not a1:
            return 0
        self.max_length = 0

        def dfs(a1):
            v1 = -1
            v2 = -1
            for v3 in a1.children:
                v4 = dfs(v3)
                if v4 > v1:
                    v2 = v1
                    v1 = v4
                elif v4 > v2:
                    v2 = v4
            if a1.children:
                v5 = 1 + v1
                if v2 >= 0:
                    self.max_length = max(self.max_length, v5 + 1 + v2)
                else:
                    self.max_length = max(self.max_length, v5)
            return 1 + v1 if v1 >= 0 else 0
        dfs(a1)
        return self.max_length
