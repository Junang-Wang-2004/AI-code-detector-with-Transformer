class Solution(object):
    def minimumFlips(self, root, result):
        INF = float('inf')

        def evaluate(node):
            if node.left is None and node.right is None:
                v = node.val
                return v, 1 - v
            if node.val == 5:
                child = node.left or node.right
                cf, ct = evaluate(child)
                return ct, cf
            cf_l, ct_l = evaluate(node.left)
            cf_r, ct_r = evaluate(node.right)
            if node.val == 2:
                c_false = cf_l + cf_r
                c_true = min(cf_l + ct_r, ct_l + cf_r, ct_l + ct_r)
            elif node.val == 3:
                c_false = min(cf_l + cf_r, cf_l + ct_r, ct_l + cf_r)
                c_true = ct_l + ct_r
            elif node.val == 4:
                c_false = min(cf_l + cf_r, ct_l + ct_r)
                c_true = min(cf_l + ct_r, ct_l + cf_r)
            else:
                c_false = c_true = INF
            return c_false, c_true

        cost_false, cost_true = evaluate(root)
        return cost_false if not result else cost_true
