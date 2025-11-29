class Solution:
    def findSecondMinimumValue(self, root):
        first = float('inf')
        second = float('inf')

        def traverse(node):
            nonlocal first, second
            if not node:
                return
            if node.val < first:
                second = first
                first = node.val
            elif node.val > first and node.val < second:
                second = node.val
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return second if second != float('inf') else -1
