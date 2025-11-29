class C1(object):

    def sumOfLeftLeaves(self, a1):
        """
        """

        def sumOfLeftLeavesHelper(a1, a2):
            if not a1:
                return 0
            if not a1.left and (not a1.right):
                return a1.val if a2 else 0
            return sumOfLeftLeavesHelper(a1.left, True) + sumOfLeftLeavesHelper(a1.right, False)
        return sumOfLeftLeavesHelper(a1, False)
