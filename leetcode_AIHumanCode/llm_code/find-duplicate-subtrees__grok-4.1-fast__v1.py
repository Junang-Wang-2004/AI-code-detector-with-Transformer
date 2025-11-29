class Solution:
    def findDuplicateSubtrees(self, root):
        counts = {}
        dups = []
        
        def traverse(node):
            if node is None:
                return None
            lrep = traverse(node.left)
            rrep = traverse(node.right)
            rep = (node.val, lrep, rrep)
            counts[rep] = counts.get(rep, 0) + 1
            if counts[rep] == 2:
                dups.append(node)
            return rep
        
        traverse(root)
        return dups
