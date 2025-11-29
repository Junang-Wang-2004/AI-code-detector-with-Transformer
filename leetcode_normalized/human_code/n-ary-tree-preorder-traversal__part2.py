class C1(object):

    def __init__(self, a1, a2):
        self.val = a1
        self.children = a2

class C2(object):

    def preorder(self, a1):
        """
        """

        def dfs(a1, a2):
            a2.append(a1.val)
            for v1 in a1.children:
                if v1:
                    dfs(v1, a2)
        v1 = []
        if a1:
            dfs(a1, v1)
        return v1
