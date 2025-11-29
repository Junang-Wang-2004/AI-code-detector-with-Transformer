class C1(object):

    def findLeaves(self, a1):
        """
        """

        def findLeavesHelper(a1, a2):
            if not a1:
                return -1
            v1 = 1 + max(findLeavesHelper(a1.left, a2), findLeavesHelper(a1.right, a2))
            if len(a2) < v1 + 1:
                a2.append([])
            a2[v1].append(a1.val)
            return v1
        v1 = []
        findLeavesHelper(a1, v1)
        return v1
