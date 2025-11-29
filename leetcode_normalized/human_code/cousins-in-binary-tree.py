class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def isCousins(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2, a3, a4):
            if not a1:
                return False
            if a1.val == a2:
                return True
            a3[0] += 1
            v1, a4[0] = (a4[0], a1)
            if dfs(a1.left, a2, a3, a4):
                return True
            a4[0] = a1
            if dfs(a1.right, a2, a3, a4):
                return True
            a4[0] = v1
            a3[0] -= 1
            return False
        v1, v2 = ([0], [0])
        v3, v4 = ([None], [None])
        return dfs(a1, a2, v1, v3) and dfs(a1, a3, v2, v4) and (v1[0] == v2[0]) and (v3[0] != v4[0])
