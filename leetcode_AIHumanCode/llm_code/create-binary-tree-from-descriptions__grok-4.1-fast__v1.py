class Solution:
    def createBinaryTree(self, descriptions):
        all_vals = set()
        childs = set()
        for par, ch, lef in descriptions:
            all_vals.add(par)
            all_vals.add(ch)
            childs.add(ch)
        rootv = (all_vals - childs).pop()
        nodedict = {v: TreeNode(v) for v in all_vals}
        for par, ch, lef in descriptions:
            p = nodedict[par]
            c = nodedict[ch]
            if lef:
                p.left = c
            else:
                p.right = c
        return nodedict[rootv]
