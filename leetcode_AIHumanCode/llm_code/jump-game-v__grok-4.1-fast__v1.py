class Solution(object):
    def maxJumps(self, arr, d):
        n = len(arr)
        if n == 0:
            return 0
        tree = [0] * (4 * n)

        def seg_update(pos, val, node=1, l=0, r=n-1):
            if l == r:
                tree[node] = val
                return
            mid = (l + r) // 2
            if pos <= mid:
                seg_update(pos, val, node * 2, l, mid)
            else:
                seg_update(pos, val, node * 2 + 1, mid + 1, r)
            tree[node] = max(tree[node * 2], tree[node * 2 + 1])

        def seg_query(ql, qr, node=1, l=0, r=n-1):
            if ql > r or qr < l:
                return 0
            if ql <= l and r <= qr:
                return tree[node]
            mid = (l + r) // 2
            return max(seg_query(ql, qr, node * 2, l, mid),
                       seg_query(ql, qr, node * 2 + 1, mid + 1, r))

        order = sorted(range(n), key=lambda x: (arr[x], x))
        ptr = 0
        result = 1
        while ptr < n:
            height = arr[order[ptr]]
            batch = []
            while ptr < n and arr[order[ptr]] == height:
                batch.append(order[ptr])
                ptr += 1
            new_values = []
            for pos in batch:
                lo = max(0, pos - d)
                hi = min(n - 1, pos + d)
                prev_max = seg_query(lo, hi)
                curr_val = 1 + prev_max
                new_values.append(curr_val)
                result = max(result, curr_val)
            for j in range(len(batch)):
                seg_update(batch[j], new_values[j])
        return result
