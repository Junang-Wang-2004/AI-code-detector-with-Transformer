class C1(object):

    def judgePoint24(self, a1):
        """
        """

        def dfs(a1):
            if len(a1) == 1:
                return a1[0] == 24
            v1 = [add, sub, mul, truediv]
            for v2 in range(len(a1)):
                for v3 in range(len(a1)):
                    if v2 == v3:
                        continue
                    v4 = [a1[k] for v5 in range(len(a1)) if v2 != v5 != v3]
                    for v6 in v1:
                        if (v6 is add or v6 is mul) and v3 > v2 or (v6 == truediv and a1[v3] == 0):
                            continue
                        v4.append(v6(a1[v2], a1[v3]))
                        if dfs(v4):
                            return True
                        v4.pop()
            return False
        return dfs(list(map(Fraction, a1)))
