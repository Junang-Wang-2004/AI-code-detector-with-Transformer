class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def smallestFromLeaf(self, a1):

        def find_min_path(a1):
            v1 = chr(ord('a') + a1.val)
            if a1.left is None and a1.right is None:
                return v1
            v2 = []
            if a1.left:
                v2.append(find_min_path(a1.left) + v1)
            if a1.right:
                v2.append(find_min_path(a1.right) + v1)
            return min(v2)
        return find_min_path(a1)
