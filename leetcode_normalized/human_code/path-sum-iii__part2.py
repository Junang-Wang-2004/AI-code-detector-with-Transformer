class C1(object):

    def pathSum(self, a1, a2):
        """
        """

        def pathSumHelper(a1, a2, a3):
            if a1 is None:
                return 0
            v1 = a2 + a1.val
            return int(v1 == a3) + pathSumHelper(a1.left, v1, a3) + pathSumHelper(a1.right, v1, a3)
        if a1 is None:
            return 0
        return pathSumHelper(a1, 0, a2) + self.pathSum(a1.left, a2) + self.pathSum(a1.right, a2)
