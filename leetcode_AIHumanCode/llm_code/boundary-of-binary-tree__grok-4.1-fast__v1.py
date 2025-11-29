class Solution:
    def boundaryOfBinaryTree(self, root):
        def add_leaves(n, path):
            if n is None:
                return
            if n.left is None and n.right is None:
                path.append(n.val)
                return
            add_leaves(n.left, path)
            add_leaves(n.right, path)

        if root is None:
            return []
        path = [root.val]
        curr = root.left
        while curr is not None and (curr.left is not None or curr.right is not None):
            path.append(curr.val)
            curr = curr.left if curr.left is not None else curr.right
        add_leaves(root.left, path)
        add_leaves(root.right, path)
        curr = root.right
        rboundary = []
        while curr is not None and (curr.left is not None or curr.right is not None):
            rboundary.append(curr.val)
            curr = curr.right if curr.right is not None else curr.left
        path.extend(reversed(rboundary))
        return path
