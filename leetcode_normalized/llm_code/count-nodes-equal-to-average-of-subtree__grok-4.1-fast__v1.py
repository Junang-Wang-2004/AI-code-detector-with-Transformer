class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def averageOfSubtree(self, a1):
        self.count = 0

        def traverse(a1):
            if not a1:
                return (0, 0)
            v1, v2 = traverse(a1.left)
            v3, v4 = traverse(a1.right)
            v5 = v1 + v3 + a1.val
            v6 = v2 + v4 + 1
            if v5 // v6 == a1.val:
                self.count += 1
            return (v5, v6)
        traverse(a1)
        return self.count
