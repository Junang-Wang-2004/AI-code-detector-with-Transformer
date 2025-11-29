class C1(object):

    def splitBST(self, a1, a2):

        def traverse(a1):
            if a1 is None:
                return [None, None]
            if a1.val <= a2:
                v1 = traverse(a1.right)
                a1.right = v1[0]
                return [a1, v1[1]]
            v1 = traverse(a1.left)
            a1.left = v1[1]
            return [v1[0], a1]
        v1 = traverse(a1)
        return (v1[0], v1[1])
