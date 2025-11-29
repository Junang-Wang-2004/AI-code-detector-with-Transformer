class C1(object):

    def kthSmallest(self, a1, a2):
        """
        """

        def gen_inorder(a1):
            if a1:
                for v1 in gen_inorder(a1.left):
                    yield v1
                yield a1.val
                for v1 in gen_inorder(a1.right):
                    yield v1
        return next(islice(gen_inorder(a1), a2 - 1, a2))
