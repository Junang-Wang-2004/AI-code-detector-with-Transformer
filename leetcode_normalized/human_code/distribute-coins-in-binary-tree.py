class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def distributeCoins(self, a1):
        """
        """

        def dfs(a1, a2):
            if not a1:
                return 0
            v1, v2 = (dfs(a1.left, a2), dfs(a1.right, a2))
            a2[0] += abs(v1) + abs(v2)
            return a1.val + v1 + v2 - 1
        v1 = [0]
        dfs(a1, v1)
        return v1[0]
