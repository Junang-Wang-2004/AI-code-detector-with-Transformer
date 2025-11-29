class Solution:
    def moveSubTree(self, root, p, q):
        def get_parent(src, tgt):
            if src == tgt:
                return None
            stk = [(src, None)]
            while stk:
                cur, prev = stk.pop()
                if cur == tgt:
                    return prev
                for kid in cur.children:
                    stk.append((kid, cur))
            return None

        def has_sub(src, tgt):
            stk = [src]
            while stk:
                cur = stk.pop()
                if cur == tgt:
                    return True
                for kid in cur.children:
                    stk.append(kid)
            return False

        pp = get_parent(root, p)
        pq = get_parent(root, q)
        if pp == q:
            return root
        p_anc_q = has_sub(p, q)
        q.children.append(p)
        if not p_anc_q:
            if pp is not None:
                pp.children.remove(p)
        else:
            pq.children.remove(q)
            if pp is None:
                root = q
            else:
                i = pp.children.index(p)
                pp.children[i] = q
        return root
