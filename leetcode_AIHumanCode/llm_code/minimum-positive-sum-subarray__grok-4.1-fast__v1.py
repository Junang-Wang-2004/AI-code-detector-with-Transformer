import bisect

class Solution:
    def minimumSumSubarray(self, nums, l, r):
        INF = float('inf')
        NINF = float('-inf')
        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
        vals = sorted(set(presum))
        m = len(vals)
        if m == 0:
            return -1
        rank_map = {vals[j]: j for j in range(m)}
        tree = [NINF] * (4 * m)
        occurrence = [0] * m

        def update_tree(node, tstart, tend, pos, newval):
            if tstart == tend:
                tree[node] = newval
                return
            tmid = (tstart + tend) // 2
            if pos <= tmid:
                update_tree(2 * node, tstart, tmid, pos, newval)
            else:
                update_tree(2 * node + 1, tmid + 1, tend, pos, newval)
            tree[node] = max(tree[2 * node], tree[2 * node + 1])

        def query_tree(node, tstart, tend, qleft, qright):
            if qright < tstart or tend < qleft:
                return NINF
            if qleft <= tstart and tend <= qright:
                return tree[node]
            tmid = (tstart + tend) // 2
            left_max = query_tree(2 * node, tstart, tmid, qleft, qright)
            right_max = query_tree(2 * node + 1, tmid + 1, tend, qleft, qright)
            return max(left_max, right_max)

        min_positive = INF
        for i in range(n):
            new_start = i - l + 1
            if new_start >= 0:
                rk = rank_map[presum[new_start]]
                occurrence[rk] += 1
                if occurrence[rk] == 1:
                    update_tree(1, 0, m - 1, rk, vals[rk])
            old_start = i - r
            if old_start >= 0:
                rk = rank_map[presum[old_start]]
                occurrence[rk] -= 1
                if occurrence[rk] == 0:
                    update_tree(1, 0, m - 1, rk, NINF)
            curr = presum[i + 1]
            split_pos = bisect.bisect_left(vals, curr) - 1
            if split_pos >= 0:
                max_less = query_tree(1, 0, m - 1, 0, split_pos)
                if max_less != NINF:
                    min_positive = min(min_positive, curr - max_less)
        return min_positive if min_positive < INF else -1
