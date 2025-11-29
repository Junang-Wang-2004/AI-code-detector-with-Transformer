# Time:  O(n)
# Space: O(h)

# Definition for Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


# Definition for NodeCopy.
class NodeCopy(object):
    def __init__(self, val=0, left=None, right=None, random=None):
        pass


class Solution(object):
    def copyRandomBinaryTree(self, root):
        """
        """
        def iter_dfs(node, callback):
            result = None
            stk = [node]
            while stk:
                node = stk.pop()
                if not node:
                    continue
                left_node, copy = callback(node)
                if not result:
                    result = copy
                stk.append(node.right)
                stk.append(left_node)
            return result
    
        def merge(node):
            copy = NodeCopy(node.val)
            node.left, copy.left = copy, node.left
            return copy.left, copy
        
        def clone(node):
            copy = node.left
            node.left.random = node.random.left if node.random else None
            node.left.right = node.right.left if node.right else None
            return copy.left, copy
        
        def split(node):
            copy = node.left
            node.left, copy.left = copy.left, copy.left.left if copy.left else None
            return node.left, copy
    
        iter_dfs(root, merge)
        iter_dfs(root, clone)
        return iter_dfs(root, split)


