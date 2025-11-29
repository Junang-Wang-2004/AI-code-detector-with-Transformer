class Solution:
    def maximumSumQueries(self, nums1, nums2, queries):
        all_b = sorted(set(nums2) | {q[1] for q in queries})
        cs = len(all_b)
        rank = {all_b[i]: cs - i for i in range(cs)}
        ft = [0] * (cs + 1)
        def ft_update(idx, val):
            while idx <= cs:
                ft[idx] = max(ft[idx], val)
                idx += idx & -idx
        def ft_query(idx):
            res = 0
            while idx > 0:
                res = max(res, ft[idx])
                idx -= idx & -idx
            return res
        pair_list = sorted(zip(nums1, nums2), key=lambda p: -p[0])
        qlist = sorted((queries[k][0], queries[k][1], k) for k in range(len(queries))), key=lambda t: -t[0])
        ans = [-1] * len(queries)
        pidx = 0
        for x, y, kidx in qlist:
            while pidx < len(pair_list) and pair_list[pidx][0] >= x:
                a, b = pair_list[pidx]
                ft_update(rank[b], a + b)
                pidx += 1
            pos = rank[y]
            mx = ft_query(pos)
            if mx > 0:
                ans[kidx] = mx
        return ans
