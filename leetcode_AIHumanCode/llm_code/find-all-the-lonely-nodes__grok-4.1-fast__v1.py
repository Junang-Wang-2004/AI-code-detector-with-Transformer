class Solution:
    def getLonelyNodes(self, root):
        lonely = []
        
        def traverse(curr):
            if not curr:
                return
            if curr.left:
                if not curr.right:
                    lonely.append(curr.left.val)
                traverse(curr.left)
            if curr.right:
                if not curr.left:
                    lonely.append(curr.right.val)
                traverse(curr.right)
        
        traverse(root)
        return lonely
