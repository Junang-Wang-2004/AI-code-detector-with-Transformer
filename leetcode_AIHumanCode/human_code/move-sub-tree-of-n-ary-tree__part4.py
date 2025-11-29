# Time:  O(n)
# Space: O(h)
# two pass solution with recursion (bad in deep tree)
class Solution2_Recu(object):
    def moveSubTree(self, root, p, q):
        """
        """
        def find_parents(node, parent, p, q, lookup):
            if node in (p, q):
                lookup[node] = parent
                if len(lookup) == 2:
                    return True
            for child in node.children:
                if find_parents(child, node, p, q, lookup):
                    return True
            return False

        def is_ancestor(node, q):
            for child in node.children:
                if node == q or is_ancestor(child, q):
                    return True
            return False

        lookup = {}
        find_parents(root, None, p, q, lookup)
        if p in lookup and lookup[p] == q:
            return root
        q.children.append(p)
        if not is_ancestor(p, q):
            lookup[p].children.remove(p)
        else:
            lookup[q].children.remove(q)
            if p == root:
                root = q
            else:
                lookup[p].children[lookup[p].children.index(p)] = q
        return root
