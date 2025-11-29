class C1(object):

    def findDuplicateSubtrees(self, a1):
        """
        """

        def postOrderTraversal(a1, a2, a3):
            if not a1:
                return ''
            v1 = '(' + postOrderTraversal(a1.left, a2, a3) + str(a1.val) + postOrderTraversal(a1.right, a2, a3) + ')'
            if a2[v1] == 1:
                a3.append(a1)
            a2[v1] += 1
            return v1
        v1 = collections.defaultdict(int)
        v2 = []
        postOrderTraversal(a1, v1, v2)
        return v2
