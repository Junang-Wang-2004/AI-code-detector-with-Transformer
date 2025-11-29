class C1(object):

    def getDirections(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2, a3):
            if a1.val == a2:
                return True
            if a1.left and dfs(a1.left, a2, a3):
                a3.append('L')
            elif a1.right and dfs(a1.right, a2, a3):
                a3.append('R')
            return a3
        v1, v2 = ([], [])
        dfs(a1, a2, v1)
        dfs(a1, a3, v2)
        while len(v1) and len(v2) and (v1[-1] == v2[-1]):
            v1.pop()
            v2.pop()
        v2.reverse()
        return ''.join(['U'] * len(v1) + v2)
