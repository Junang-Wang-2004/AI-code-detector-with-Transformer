class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructFromPrePost(self, pre, post):
        val_to_postidx = {post[i]: i for i in range(len(post))}
        def build(pre_lo, post_lo, subtree_size):
            if subtree_size == 0:
                return None
            curr = TreeNode(pre[pre_lo])
            if subtree_size > 1:
                left_subtree_size = val_to_postidx[pre[pre_lo + 1]] - post_lo + 1
                curr.left = build(pre_lo + 1, post_lo, left_subtree_size)
                curr.right = build(pre_lo + 1 + left_subtree_size,
                                   post_lo + left_subtree_size,
                                   subtree_size - left_subtree_size - 1)
            return curr
        return build(0, 0, len(pre))
