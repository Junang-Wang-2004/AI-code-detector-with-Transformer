class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def maxProduct(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        def dfs(a1, a2, a3):
            if not a1:
                return 0
            v1 = dfs(a1.left, a2, a3) + dfs(a1.right, a2, a3) + a1.val
            a3[0] = max(a3[0], v1 * (a2 - v1))
            return v1
        v2 = [0]
        dfs(a1, dfs(a1, 0, v2), v2)
        return v2[0] % v1
