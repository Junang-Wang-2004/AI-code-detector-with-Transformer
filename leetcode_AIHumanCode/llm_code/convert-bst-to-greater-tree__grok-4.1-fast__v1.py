class Solution:
    def convertBST(self, root):
        total = 0
        stk = []
        node = root
        while stk or node:
            while node:
                stk.append(node)
                node = node.right
            node = stk.pop()
            node.val += total
            total = node.val
            node = node.left
        return root
