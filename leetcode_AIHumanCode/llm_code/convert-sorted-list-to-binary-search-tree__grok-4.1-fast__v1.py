class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortedListToBST(self, head):
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next
        
        def build_tree(left_idx, right_idx):
            if left_idx >= right_idx:
                return None
            mid_idx = (left_idx + right_idx) // 2
            root = TreeNode(vals[mid_idx])
            root.left = build_tree(left_idx, mid_idx)
            root.right = build_tree(mid_idx + 1, right_idx)
            return root
        
        return build_tree(0, len(vals))
