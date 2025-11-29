class C1(object):

    def __init__(self, a1=0, a2=None, a3=None, a4=None):
        self.val = a1
        self.left = a2
        self.right = a3
        self.random = a4

class C2(object):

    def __init__(self, a1=0, a2=None, a3=None, a4=None):
        pass

class C3(object):

    def copyRandomBinaryTree(self, a1):
        """
        """

        def iter_dfs(a1, a2):
            v1 = None
            v2 = [a1]
            while v2:
                a1 = v2.pop()
                if not a1:
                    continue
                v4, v5 = a2(a1)
                if not v1:
                    v1 = v5
                v2.append(a1.right)
                v2.append(v4)
            return v1

        def merge(a1):
            v1 = C2(a1.val)
            a1.left, v1.left = (v1, a1.left)
            return (v1.left, v1)

        def clone(a1):
            v1 = a1.left
            a1.left.random = a1.random.left if a1.random else None
            a1.left.right = a1.right.left if a1.right else None
            return (v1.left, v1)

        def split(a1):
            v1 = a1.left
            a1.left, v1.left = (v1.left, v1.left.left if v1.left else None)
            return (a1.left, v1)
        iter_dfs(a1, merge)
        iter_dfs(a1, clone)
        return iter_dfs(a1, split)
