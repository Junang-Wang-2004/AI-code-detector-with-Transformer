# Time:  O(n * m * l + l * tlogt + l * t^2), m is the max number of folders in a path,
#                                          , n is the number of paths
#                                          , l is the max length of folder name
#                                          , t is the size of trie
# Space: O(l * t^2)
import collections


class Solution2(object):
    def deleteDuplicateFolder(self, paths):
        """
        """
        def mark(node, lookup):
            serialized_tree = "(" + "".join(subfolder + mark(child, lookup) for subfolder, child in sorted(node.items()) if child != "_del") + ")"
            if serialized_tree != "()":
                if serialized_tree in lookup:
                    lookup[serialized_tree]["_del"]
                    node["_del"]
                else:
                    lookup[serialized_tree] = node
            return serialized_tree
        
        def sweep(node, path, result):
            if path:
                result.append(path[:])
            for subfolder, child in node.items():
                if "_del" in child:
                    continue
                path.append(subfolder)
                sweep(child, path, result)
                path.pop()

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for path in paths:
            reduce(dict.__getitem__, path, trie)
        mark(trie, {})
        result = []
        sweep(trie, [], result)
        return result
