# Time:  O(n * m * l + tlogt + l * t), m is the max number of folders in a path,
#                                    , n is the number of paths
#                                    , l is the max length of folder name
#                                    , t is the size of trie
# Space: O(l * t)

import collections
from functools import reduce


class Solution(object):
    def deleteDuplicateFolder(self, paths):
        """
        """
        def mark(node, lookup, node_ids):
            id_pairs = []
            for subfolder_id, child in node.items():
                if child == "_del":
                    continue
                id_pairs.append((subfolder_id, mark(child, lookup, node_ids)))
            id_pairs.sort()
            node_id = node_ids[tuple(id_pairs)]
            if node_id:
                if node_id in lookup:
                    lookup[node_id]["_del"]
                    node["_del"]
                else:
                    lookup[node_id] = node
            return node_id

        def sweep(node, id_folders, path, result):
            if path:
                result.append([id_folders[i] for i in path])
            for subfolder_id, child in node.items():
                if "_del" in child:
                    continue
                path.append(subfolder_id)
                sweep(child, id_folders, path, result)
                path.pop()

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        folder_ids = collections.defaultdict()
        folder_ids.default_factory = folder_ids.__len__
        id_folders = {}
        for path in paths:
            node = trie
            for folder in path:
                if folder_ids[folder] not in id_folders:
                    id_folders[folder_ids[folder]] = folder
                node = node[folder_ids[folder]]
        node_ids = collections.defaultdict()
        node_ids.default_factory = node_ids.__len__
        mark(trie, {}, node_ids)
        result = []
        sweep(trie, id_folders, [], result)
        return result


