class C1(object):

    def findTilt(self, a1):
        """
        """

        def postOrderTraverse(a1, a2):
            if not a1:
                return (0, a2)
            v1, a2 = postOrderTraverse(a1.left, a2)
            v3, a2 = postOrderTraverse(a1.right, a2)
            a2 += abs(v1 - v3)
            return (v1 + v3 + a1.val, a2)
        return postOrderTraverse(a1, 0)[1]
