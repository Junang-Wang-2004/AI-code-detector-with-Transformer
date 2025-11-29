# Time:  O(n)
# Space: O(h)
# one pass solution with recursion (bad in deep tree)
class Solution_Recu(object):
    def moveSubTree(self, root, p, q):
        """
        """
        def find_parents(node, parent, p, q, is_ancestor, lookup):
            if node in (p, q):
                lookup[node] = parent
                if len(lookup) == 2:
                    return True, is_ancestor
            for child in node.children:
                found, new_is_ancestor = find_parents(child, node, p, q, is_ancestor or node == p, lookup)
                if found:
                    return True, new_is_ancestor
            return False, False

        lookup = {}
        is_ancestor = find_parents(root, None, p, q, False, lookup)[1]
        if p in lookup and lookup[p] == q:
            return root
        q.children.append(p)
        if not is_ancestor:
            lookup[p].children.remove(p)
        else:
            lookup[q].children.remove(q)
            if p == root:
                root = q
            else:
                lookup[p].children[lookup[p].children.index(p)] = q
        return root


