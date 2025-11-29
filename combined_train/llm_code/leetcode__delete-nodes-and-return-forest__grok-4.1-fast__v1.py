class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def delNodes(self, a1, a2):
        v1 = set(a2)
        v2 = []

        def process(a1):
            if a1 is None:
                return None
            a1.left = process(a1.left)
            a1.right = process(a1.right)
            if a1.val in v1:
                if a1.left is not None:
                    v2.append(a1.left)
                if a1.right is not None:
                    v2.append(a1.right)
                return None
            return a1
        v3 = process(a1)
        if v3 is not None:
            v2.append(v3)
        return v2
