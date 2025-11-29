class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def increasingBST(self, a1):

        def traverse(a1):
            nonlocal start, prev_node
            if not a1:
                return
            traverse(a1.left)
            if prev_node:
                prev_node.right = a1
            else:
                v1 = a1
            a1.left = None
            v2 = a1
            traverse(a1.right)
        v1 = v2 = None
        traverse(a1)
        return v1
