class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def minCameraCover(self, a1):
        """
        """
        v1, v2, v3 = list(range(3))

        def dfs(a1, a2):
            v1 = dfs(a1.left, a2) if a1.left else v2
            v2 = dfs(a1.right, a2) if a1.right else v2
            if v1 == v1 or v2 == v1:
                a2[0] += 1
                return v3
            if v1 == v3 or v2 == v3:
                return v2
            return v1
        v4 = [0]
        if dfs(a1, v4) == v1:
            v4[0] += 1
        return v4[0]
