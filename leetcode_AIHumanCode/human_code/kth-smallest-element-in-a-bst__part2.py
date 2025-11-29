# Time:  O(max(h, k))
# Space: O(h)

class Solution2(object):
    def kthSmallest(self, root, k):
        """
        """
        def gen_inorder(root):
            if root:
                for n in gen_inorder(root.left):
                    yield n

                yield root.val

                for n in gen_inorder(root.right):
                    yield n

        return next(islice(gen_inorder(root), k-1, k))
