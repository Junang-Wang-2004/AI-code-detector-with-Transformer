# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def constructFromPrePost(self, pre, post):
        """
        """
        def constructFromPrePostHelper(pre, pre_s, pre_e, post, post_s, post_e, post_entry_idx_map):
            if pre_s >= pre_e or post_s >= post_e:
                return None
            node = TreeNode(pre[pre_s])
            if pre_e-pre_s > 1:
                left_tree_size = post_entry_idx_map[pre[pre_s+1]]-post_s+1
                node.left = constructFromPrePostHelper(pre, pre_s+1, pre_s+1+left_tree_size, 
                                                       post, post_s, post_s+left_tree_size,
                                                       post_entry_idx_map)
                node.right = constructFromPrePostHelper(pre, pre_s+1+left_tree_size, pre_e,
                                                        post, post_s+left_tree_size, post_e-1,
                                                        post_entry_idx_map)
            return node

        post_entry_idx_map = {}
        for i, val in enumerate(post):
            post_entry_idx_map[val] = i
        return constructFromPrePostHelper(pre, 0, len(pre), post, 0, len(post), post_entry_idx_map)

