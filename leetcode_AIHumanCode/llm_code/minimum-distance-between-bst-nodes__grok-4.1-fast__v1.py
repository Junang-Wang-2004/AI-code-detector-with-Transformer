class Solution:
    def minDiffInBST(self, root):
        stk = []
        node = root
        last = float('-inf')
        ans = float('inf')
        while stk or node:
            while node:
                stk.append(node)
                node = node.left
            node = stk.pop()
            ans = min(ans, node.val - last)
            last = node.val
            node = node.right
        return ans
