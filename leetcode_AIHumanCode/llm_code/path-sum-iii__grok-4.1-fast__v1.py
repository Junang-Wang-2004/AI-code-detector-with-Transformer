class Solution:
    def pathSum(self, root, sum):
        count = 0
        prefix_map = {0: 1}

        def traverse(node, curr_prefix):
            nonlocal count
            if not node:
                return
            curr_prefix += node.val
            count += prefix_map.get(curr_prefix - sum, 0)
            prefix_map[curr_prefix] = prefix_map.get(curr_prefix, 0) + 1
            traverse(node.left, curr_prefix)
            traverse(node.right, curr_prefix)
            prefix_map[curr_prefix] -= 1
            if not prefix_map[curr_prefix]:
                del prefix_map[curr_prefix]

        traverse(root, 0)
        return count
