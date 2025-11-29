class Solution(object):
    def isSubtree(self, s, t):
        def preorder(node):
            if node is None:
                return "#"
            return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
        s_str = preorder(s)
        t_str = preorder(t)
        return t_str in s_str
