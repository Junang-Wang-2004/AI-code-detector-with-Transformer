# Time:  O(n)
# Space: O(h)
# two pass solution without recursion
class Solution2(object):
    def moveSubTree(self, root, p, q):
        """
        """
        def iter_find_parents(node, parent, p, q, lookup):
            stk = [(1, [node, None])]
            while stk:
                step, params = stk.pop()
                if step == 1:
                    node, parent = params
                    if node in (p, q):
                        lookup[node] = parent
                        if len(lookup) == 2:
                            return
                    stk.append((2, [node, reversed(node.children)]))
                else:
                    node, it = params
                    child = next(it, None)
                    if not child:
                        continue
                    stk.append((2, [node, it]))
                    stk.append((1, [child, node]))

        def iter_is_ancestor(node, q):
            stk = [(1, [node])]
            while stk:
                step, params = stk.pop()
                if step == 1:
                    node = params[0]
                    stk.append((2, [reversed(node.children)]))
                else:
                    it = params[0]
                    child = next(it, None)
                    if not child:
                        continue
                    if child == q:
                        return True
                    stk.append((2, [it]))
                    stk.append((1, [child]))
            return False

        lookup = {}
        iter_find_parents(root, None, p, q, lookup)
        if p in lookup and lookup[p] == q:
            return root
        q.children.append(p)
        if not iter_is_ancestor(p, q):
            lookup[p].children.remove(p)
        else:
            lookup[q].children.remove(q)
            if p == root:
                root = q
            else:
                lookup[p].children[lookup[p].children.index(p)] = q
        return root


