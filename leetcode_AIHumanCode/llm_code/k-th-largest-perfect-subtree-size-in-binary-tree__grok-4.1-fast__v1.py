class Solution:
    def kthLargestPerfectSubtree(self, root, k):
        vals = []
        def evaluate(nd):
            if not nd:
                return 0
            lsz = evaluate(nd.left)
            rsz = evaluate(nd.right)
            perf = lsz + rsz + 1 if lsz == rsz >= 0 else -1
            vals.append(perf)
            return perf
        evaluate(root)
        goods = sorted(s for s in vals if s > 0)[::-1]
        return goods[k - 1] if k <= len(goods) else -1
