# Time:  O(n)
# Space: O(h)
class Solution_Recu(object):
    def copyRandomBinaryTree(self, root):
        """
        """
        def dfs(node, callback):
            if not node:
                return None
            left_node, copy = callback(node)
            dfs(left_node, callback)
            dfs(node.right, callback) 
            return copy
    
        def merge(node):
            copy = NodeCopy(node.val)
            node.left, copy.left = copy, node.left
            return copy.left, copy
        
        def clone(node):
            copy = node.left
            node.left.random = node.random.left if node.random else None
            node.left.right = node.right.left if node.right else None
            return copy.left, copy
        
        def split(node):
            copy = node.left
            node.left, copy.left = copy.left, copy.left.left if copy.left else None
            return node.left, copy
    
        dfs(root, merge)
        dfs(root, clone)
        return dfs(root, split)


