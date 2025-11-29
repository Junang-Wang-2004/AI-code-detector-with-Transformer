# Time:  O(n * min(h, l))
# Space: O(h)
# dfs solution
class Solution2(object):
    def isSubPath(self, head, root):
        """
        """
        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            return root.val == head.val and \
                   (dfs(head.__next__, root.left) or 
                    dfs(head.__next__, root.right))
    
        if not head:
            return True
        if not root:
            return False
        return dfs(head, root) or \
               self.isSubPath(head, root.left) or \
               self.isSubPath(head, root.right)
