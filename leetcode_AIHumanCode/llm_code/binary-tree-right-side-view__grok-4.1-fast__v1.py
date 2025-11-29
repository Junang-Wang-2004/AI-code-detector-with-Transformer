class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        view = []
        stack = [(root, 0)]
        max_depth = -1
        while stack:
            node, depth = stack.pop()
            if depth > max_depth:
                view.append(node.val)
                max_depth = depth
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return view
