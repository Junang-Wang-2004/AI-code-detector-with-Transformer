class C1(object):

    def isSubtree(self, a1, a2):

        def preorder(a1):
            if a1 is None:
                return '#'
            return str(a1.val) + ',' + preorder(a1.left) + ',' + preorder(a1.right)
        v1 = preorder(a1)
        v2 = preorder(a2)
        return v2 in v1
