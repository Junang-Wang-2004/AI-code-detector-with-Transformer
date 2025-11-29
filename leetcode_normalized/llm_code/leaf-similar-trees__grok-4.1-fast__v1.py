class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def leafSimilar(self, a1, a2):

        def extract_leaves(a1):
            if a1 is None:
                return []
            if a1.left is None and a1.right is None:
                return [a1.val]
            v1 = extract_leaves(a1.left)
            v2 = extract_leaves(a1.right)
            return v1 + v2
        v1 = extract_leaves(a1)
        v2 = extract_leaves(a2)
        return v1 == v2
