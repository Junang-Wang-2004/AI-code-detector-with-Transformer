class Solution:
    def countPairs(self, n, edges, queries):
        deg = [0] * (n + 1)
        adj_pairs = {}
        for x, y in edges:
            deg[x] += 1
            deg[y] += 1
            mn, mx = min(x, y), max(x, y)
            ky = (mn, mx)
            adj_pairs[ky] = adj_pairs.get(ky, 0) + 1
        node_degs = [deg[i] for i in range(1, n + 1)]
        if not node_degs:
            return [0] * len(queries)
        mx_deg = max(node_degs)
        buckets = [0] * (2 * (mx_deg + 2))
        freq_map = {}
        for val in node_degs:
            freq_map[val] = freq_map.get(val, 0) + 1
        deg_list = sorted(freq_map)
        for i in range(len(deg_list)):
            d_a = deg_list[i]
            cnt_a = freq_map[d_a]
            for j in range(i, len(deg_list)):
                d_b = deg_list[j]
                cnt_b = freq_map[d_b]
                total = d_a + d_b
                if i == j:
                    buckets[total] += cnt_a * (cnt_a - 1) // 2
                else:
                    buckets[total] += cnt_a * cnt_b
        for (a, b), mult_cnt in adj_pairs.items():
            orig_sum = deg[a] + deg[b]
            adj_sum = orig_sum - mult_cnt
            buckets[orig_sum] -= 1
            if adj_sum >= 0:
                buckets[adj_sum] += 1
        for pos in range(len(buckets) - 2, -1, -1):
            buckets[pos] += buckets[pos + 1]
        res = []
        for lim in queries:
            tgt = lim + 1
            res.append(buckets[tgt] if tgt < len(buckets) else 0)
        return res
