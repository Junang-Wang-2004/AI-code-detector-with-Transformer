class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def preorderTraversal(self, a1):
        v1 = []

        def dfs(a1):
            if a1:
                v1.append(a1.val)
                dfs(a1.left)
                dfs(a1.right)
        dfs(a1)
        return v1
