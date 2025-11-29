class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = list(children) if children else []


class Solution:
    def cloneTree(self, root):
        if not root:
            return None
        stack = []
        newroot = Node(root.val)
        stack.append([root, newroot, 0])
        while stack:
            oldnode, newnode, idx = stack[-1]
            if idx >= len(oldnode.children):
                stack.pop()
            else:
                kid = oldnode.children[idx]
                newkid = Node(kid.val)
                newnode.children.append(newkid)
                stack[-1][2] += 1
                stack.append([kid, newkid, 0])
        return newroot
