# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# iterative stack solution
class Solution(object):
    def recoverFromPreorder(self, S):
        """
        """
        i = 0
        stack = []
        while i < len(S):
            level = 0
            while i < len(S) and S[i] == '-':
                level += 1
                i += 1
            while len(stack) > level:
                stack.pop()
            val = []
            while i < len(S) and S[i] != '-':
                val.append(S[i])
                i += 1
            node = TreeNode(int("".join(val)))
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]


