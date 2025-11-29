class Solution:
    def countUnivalSubtrees(self, root):
        self.total = 0
        
        def check_subtree(node):
            if not node:
                return True
            
            left_ok = check_subtree(node.left)
            right_ok = check_subtree(node.right)
            
            current_ok = (left_ok and right_ok and
                          (node.left is None or node.val == node.left.val) and
                          (node.right is None or node.val == node.right.val))
            
            if current_ok:
                self.total += 1
                return True
            
            return False
        
        check_subtree(root)
        return self.total
