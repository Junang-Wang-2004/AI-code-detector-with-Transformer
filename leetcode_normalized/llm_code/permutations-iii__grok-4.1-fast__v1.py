class C1:

    def permute(self, a1):
        v1 = []
        v2 = [False] * (a1 + 1)

        def dfs(a1):
            if len(a1) == a1:
                v1.append(list(a1))
                return
            for v1 in range(1, a1 + 1):
                if not v2[v1] and (not a1 or a1[-1] % 2 != v1 % 2):
                    v2[v1] = True
                    a1.append(v1)
                    dfs(a1)
                    a1.pop()
                    v2[v1] = False
        dfs([])
        return v1
