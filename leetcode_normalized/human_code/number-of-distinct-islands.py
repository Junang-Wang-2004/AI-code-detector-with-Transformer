class C1(object):

    def numDistinctIslands(self, a1):
        """
        """
        v1 = {'l': [-1, 0], 'r': [1, 0], 'u': [0, 1], 'd': [0, -1]}

        def dfs(a1, a2, a3, a4):
            if not (0 <= a1 < len(a3) and 0 <= a2 < len(a3[0]) and (a3[a1][a2] > 0)):
                return False
            a3[a1][a2] *= -1
            for v1, v2 in v1.items():
                a4.append(v1)
                dfs(a1 + v2[0], a2 + v2[1], a3, a4)
            return True
        v2 = set()
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                v5 = []
                if dfs(v3, v4, a1, v5):
                    v2.add(''.join(v5))
        return len(v2)
