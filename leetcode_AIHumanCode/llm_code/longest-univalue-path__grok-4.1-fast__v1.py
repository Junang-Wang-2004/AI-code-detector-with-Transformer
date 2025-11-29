class Solution:
    def longestUnivaluePath(self, root):
        max_path = 0
        def traverse(curr):
            nonlocal max_path
            if not curr:
                return 0
            l_path = traverse(curr.left)
            r_path = traverse(curr.right)
            ext_l = l_path + 1 if curr.left and curr.val == curr.left.val else 0
            ext_r = r_path + 1 if curr.right and curr.val == curr.right.val else 0
            max_path = max(max_path, ext_l + ext_r)
            return max(ext_l, ext_r)
        traverse(root)
        return max_path
