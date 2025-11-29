class C1(object):

    def crackSafe(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3, a4):
            for v1 in range(a1):
                v2 = a2 + str(v1)
                if v2 not in a3:
                    a3.add(v2)
                    a4.append(str(v1))
                    dfs(a1, v2[1:], a3, a4)
                    break
        v1 = [str(a2 - 1)] * (a1 - 1)
        v2 = set()
        dfs(a2, ''.join(v1), v2, v1)
        return ''.join(v1)
