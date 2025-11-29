class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def diameterOfBinaryTree(self, a1):
        if not a1:
            return 0
        v1 = 0

        def traverse(a1):
            nonlocal max_path
            if not a1:
                return 0
            v1 = traverse(a1.left)
            v2 = traverse(a1.right)
            v3 = max(v3, v1 + v2)
            return 1 + max(v1, v2)
        traverse(a1)
        return v1
