class Solution:
    def lowestCommonAncestor(self, root, nodes):
        target_set = set(nodes)
        num_targets = len(targets_set)
        result = [None]

        def post_order_traverse(curr_node):
            if curr_node is None:
                return 0
            left_count = post_order_traverse(curr_node.left)
            right_count = post_order_traverse(curr_node.right)
            node_count = 1 if curr_node in target_set else 0
            subtree_total = left_count + right_count + node_count
            if subtree_total == num_targets and result[0] is None:
                result[0] = curr_node
            return subtree_total

        post_order_traverse(root)
        return result[0]
