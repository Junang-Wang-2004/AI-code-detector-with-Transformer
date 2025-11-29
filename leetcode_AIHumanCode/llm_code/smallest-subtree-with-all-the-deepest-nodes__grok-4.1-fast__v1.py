class Solution:
    def subtreeWithAllDeepest(self, root):
        def recurse(cur):
            if not cur:
                return None, 0
            lroot, lh = recurse(cur.left)
            rroot, rh = recurse(cur.right)
            md = max(lh, rh)
            if lh == md == rh:
                return cur, md + 1
            if lh == md:
                return lroot, md + 1
            return rroot, md + 1

        return recurse(root)[0]
