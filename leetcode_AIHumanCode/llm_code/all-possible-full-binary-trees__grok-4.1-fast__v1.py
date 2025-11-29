class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.cache = {}

    def allPossibleFBT(self, n):
        def generate_trees(node_count):
            if node_count % 2 == 0 or node_count < 1:
                return []
            if node_count == 1:
                return [TreeNode()]
            if node_count in self.cache:
                return self.cache[node_count]
            possible_trees = []
            for left_count in range(1, node_count, 2):
                left_subtrees = generate_trees(left_count)
                right_subtrees = generate_trees(node_count - 1 - left_count)
                for left_tree in left_subtrees:
                    for right_tree in right_subtrees:
                        new_root = TreeNode()
                        new_root.left = left_tree
                        new_root.right = right_tree
                        possible_trees.append(new_root)
            self.cache[node_count] = possible_trees
            return possible_trees

        return generate_trees(n)
