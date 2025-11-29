class Solution:
    def copyRandomBinaryTree(self, root):
        mapping = {}
        
        def construct(ptr):
            if not ptr:
                return None
            if ptr in mapping:
                return mapping[ptr]
            clone = NodeCopy(ptr.val)
            mapping[ptr] = clone
            clone.left = construct(ptr.left)
            clone.right = construct(ptr.right)
            clone.random = construct(ptr.random)
            return clone
        
        return construct(root)
