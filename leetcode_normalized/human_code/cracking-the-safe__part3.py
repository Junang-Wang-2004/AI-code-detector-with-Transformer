class C1(object):

    def crackSafe(self, a1, a2):
        """
        """
        v1 = a2 ** (a1 - 1)

        def dfs(a1, a2, a3, a4):
            for v1 in reversed(range(a1)):
                v2 = a2 * a1 + v1
                if v2 not in a3:
                    a3.add(v2)
                    a4.append(str(v1))
                    dfs(a1, v2 % v1, a3, a4)
                    break
        v2 = 0
        v3 = [str(0)] * (a1 - 1)
        v4 = set()
        dfs(a2, v2, v4, v3)
        return ''.join(v3)
