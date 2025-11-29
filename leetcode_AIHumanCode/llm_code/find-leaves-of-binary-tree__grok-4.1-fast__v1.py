class Solution:
    def findLeaves(self, root):
        if not root:
            return []

        heights = {}

        def get_height(node):
            if node is None:
                return -1
            if node in heights:
                return heights[node]
            l = get_height(node.left)
            r = get_height(node.right)
            heights[node] = 1 + max(l, r)
            return heights[node]

        get_height(root)
        max_height = heights[root]
        groups = [[] for _ in range(max_height + 1)]

        def assign(node):
            if node is None:
                return
            assign(node.left)
            assign(node.right)
            groups[heights[node]].append(node.val)

        assign(root)
        return groups
