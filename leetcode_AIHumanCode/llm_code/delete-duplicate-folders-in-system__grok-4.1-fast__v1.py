import collections

class Solution:
    def deleteDuplicateFolder(self, paths):
        TreeNode = lambda: collections.defaultdict(TreeNode)
        root = TreeNode()

        for folder_path in paths:
            current = root
            for folder_name in folder_path:
                current = current[folder_name]

        structure_map = {}

        def get_structure_signature(tree_node):
            child_signatures = []
            for child_name, child_node in sorted(tree_node.items()):
                if '_remove' in child_node:
                    continue
                child_sig = get_structure_signature(child_node)
                child_signatures.append((child_name, child_sig))
            sig = tuple(child_signatures)
            if sig:
                if sig in structure_map:
                    structure_map[sig]['_remove'] = True
                    tree_node['_remove'] = True
                else:
                    structure_map[sig] = tree_node
            return sig

        get_structure_signature(root)

        remaining_paths = []

        def traverse(tree_node, path_so_far):
            for child_name, child_node in tree_node.items():
                if '_remove' in child_node:
                    continue
                path_so_far.append(child_name)
                remaining_paths.append(list(path_so_far))
                traverse(child_node, path_so_far)
                path_so_far.pop()

        traverse(root, [])
        return remaining_paths
