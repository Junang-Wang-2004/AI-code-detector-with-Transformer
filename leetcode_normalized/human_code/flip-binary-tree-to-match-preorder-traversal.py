class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def flipMatchVoyage(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3, a4):
            if not a1:
                return True
            if a1.val != a2[a3[0]]:
                return False
            a3[0] += 1
            if a1.left and a1.left.val != a2[a3[0]]:
                a4.append(a1.val)
                return dfs(a1.right, a2, a3, a4) and dfs(a1.left, a2, a3, a4)
            return dfs(a1.left, a2, a3, a4) and dfs(a1.right, a2, a3, a4)
        v1 = []
        return v1 if dfs(a1, a2, [0], v1) else [-1]
