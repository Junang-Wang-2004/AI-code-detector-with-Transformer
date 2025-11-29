# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubPath(self, lst_head, tree_root):
        if not lst_head:
            return True
        
        pattern = []
        curr = lst_head
        while curr:
            pattern.append(curr.val)
            curr = curr.next
        
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        def search(node, match_idx):
            if not node:
                return False
            while match_idx < m and pattern[match_idx] != node.val:
                if match_idx == 0:
                    break
                match_idx = lps[match_idx - 1]
            if match_idx < m and pattern[match_idx] == node.val:
                match_idx += 1
            if match_idx == m:
                return True
            return search(node.left, match_idx) or search(node.right, match_idx)
        
        return search(tree_root, 0)
