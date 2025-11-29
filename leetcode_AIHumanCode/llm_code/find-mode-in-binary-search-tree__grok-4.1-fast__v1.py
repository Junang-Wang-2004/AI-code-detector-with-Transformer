class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        self.modes = []
        self.max_count = 0
        self.current_count = 0
        self.previous = None

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if self.previous is None:
                self.current_count = 1
            elif node.val == self.previous.val:
                self.current_count += 1
            else:
                self.current_count = 1
            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.modes = [node.val]
            elif self.current_count == self.max_count:
                self.modes.append(node.val)
            self.previous = node
            inorder(node.right)

        inorder(root)
        return self.modes
