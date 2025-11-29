# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        def construct(depth, pos):
            if pos >= len(S):
                return None, pos
            cur_pos = pos
            dash_count = 0
            while cur_pos < len(S) and S[cur_pos] == '-':
                dash_count += 1
                cur_pos += 1
            if dash_count != depth:
                return None, pos
            num_start = cur_pos
            while cur_pos < len(S) and S[cur_pos] != '-':
                cur_pos += 1
            new_node = TreeNode(int(S[num_start:cur_pos]))
            left_child, pos = construct(depth + 1, cur_pos)
            new_node.left = left_child
            right_child, pos = construct(depth + 1, pos)
            new_node.right = right_child
            return new_node, pos

        root, _ = construct(0, 0)
        return root
