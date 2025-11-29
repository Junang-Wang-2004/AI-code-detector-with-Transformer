class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        val_to_idx = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = [0]

        def construct(left_bound, right_bound):
            if left_bound > right_bound:
                return None
            curr_root_val = preorder[pre_idx[0]]
            pre_idx[0] += 1
            curr_root = TreeNode(curr_root_val)
            root_pos_inorder = val_to_idx[curr_root_val]
            curr_root.left = construct(left_bound, root_pos_inorder - 1)
            curr_root.right = construct(root_pos_inorder + 1, right_bound)
            return curr_root

        return construct(0, len(inorder) - 1)
