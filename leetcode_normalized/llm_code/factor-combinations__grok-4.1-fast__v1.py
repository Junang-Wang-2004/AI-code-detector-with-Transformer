class C1(object):

    def getFactors(self, a1):
        v1 = []

        def dfs(a1, a2, a3):
            v1 = int(a1 ** 0.5) + 1
            for v2 in range(a2, v1):
                if a1 % v2 == 0:
                    a3.append(v2)
                    dfs(a1 // v2, v2, a3)
                    a3.pop()
            if a1 >= a2:
                a3.append(a1)
                if len(a3) >= 2:
                    v1.append(list(a3))
                a3.pop()
        dfs(a1, 2, [])
        return v1
