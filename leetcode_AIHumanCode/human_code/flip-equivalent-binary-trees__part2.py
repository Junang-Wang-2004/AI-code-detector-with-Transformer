# Time:  O(n)
# Space: O(h)
# iterative dfs solution
class Solution2(object):
    def flipEquiv(self, root1, root2):
        """
        """
        stk1, stk2 = [root1], [root2]
        while stk1 and stk2:
            node1, node2 = stk1.pop(), stk2.pop()
            if not node1 and not node2:
                continue 
            if not node1 or not node2 or node1.val != node2.val:
                return False
            if (not node1.left and not node2.right) or \
               (node1.left and node2.right and node1.left.val == node2.right.val):
                stk1.extend([node1.right, node1.left])
            else:
                stk1.extend([node1.left, node1.right])
            stk2.extend([node2.left, node2.right])
        return not stk1 and not stk2


