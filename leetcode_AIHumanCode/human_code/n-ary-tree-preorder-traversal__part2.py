# Time:  O(n)
# Space: O(h)

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution2(object):
    def preorder(self, root):
        """
        """
        def dfs(root, result):
            result.append(root.val)
            for child in root.children:
                if child:
                    dfs(child, result)
        
        result = []
        if root:
            dfs(root, result)
        return result

