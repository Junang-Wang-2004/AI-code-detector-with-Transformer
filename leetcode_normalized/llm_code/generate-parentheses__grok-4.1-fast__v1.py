class C1:

    def generateParenthesis(self, a1):
        v1 = [[] for v2 in range(a1 + 1)]
        v1[0] = ['']
        for v3 in range(1, a1 + 1):
            v4 = []
            for v5 in range(v3):
                for v6 in v1[v5]:
                    for v7 in v1[v3 - 1 - v5]:
                        v4.append('(' + v6 + ')' + v7)
            v1[v3] = v4
        return v1[a1]
