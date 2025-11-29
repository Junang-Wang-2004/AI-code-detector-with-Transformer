class C1(object):

    def pyramidTransition(self, a1, a2):
        """
        """

        def pyramidTransitionHelper(a1, a2, a3):

            def dfs(a1, a2, a3, a4, a5):
                if a4 == len(a1) - 1:
                    return pyramidTransitionHelper(''.join(a3), a2, a5)
                for v1 in a2[ord(a1[a4]) - ord('A')][ord(a1[a4 + 1]) - ord('A')]:
                    a3[a4] = chr(v1 + ord('A'))
                    if dfs(a1, a2, a3, a4 + 1, a5):
                        return True
                return False
            if len(a1) == 1:
                return True
            if a1 in a3:
                return False
            a3.add(a1)
            for v1 in range(len(a1) - 1):
                if not a2[ord(a1[v1]) - ord('A')][ord(a1[v1 + 1]) - ord('A')]:
                    return False
            v2 = ['A'] * (len(a1) - 1)
            return dfs(a1, a2, v2, 0, a3)
        v1 = [[[] for v2 in range(7)] for v2 in range(7)]
        for v3 in a2:
            v1[ord(v3[0]) - ord('A')][ord(v3[1]) - ord('A')].append(ord(v3[2]) - ord('A'))
        return pyramidTransitionHelper(a1, v1, set())
