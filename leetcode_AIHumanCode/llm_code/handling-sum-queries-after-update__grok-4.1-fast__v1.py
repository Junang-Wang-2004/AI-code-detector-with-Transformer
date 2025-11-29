class Solution:
    def handleQuery(self, nums1, nums2, queries):
        n = len(nums1)
        cur_total = sum(nums2)
        res = []
        tr = [0] * (4 * n)
        lz = [0] * (4 * n)

        def construct(idx, lo, hi):
            if lo == hi:
                tr[idx] = nums1[lo]
                return
            md = (lo + hi) // 2
            construct(2 * idx, lo, md)
            construct(2 * idx + 1, md + 1, hi)
            tr[idx] = tr[2 * idx] + tr[2 * idx + 1]

        def push_down(idx, lo, hi):
            if lz[idx]:
                tr[idx] = (hi - lo + 1) - tr[idx]
                if lo != hi:
                    lz[2 * idx] ^= 1
                    lz[2 * idx + 1] ^= 1
                lz[idx] = 0

        def range_flip(idx, lo, hi, left, right):
            push_down(idx, lo, hi)
            if lo > hi or lo > right or hi < left:
                return
            if left <= lo and hi <= right:
                lz[idx] ^= 1
                push_down(idx, lo, hi)
                return
            md = (lo + hi) // 2
            range_flip(2 * idx, lo, md, left, right)
            range_flip(2 * idx + 1, md + 1, hi, left, right)
            tr[idx] = tr[2 * idx] + tr[2 * idx + 1]

        def get_sum(idx, lo, hi, left, right):
            push_down(idx, lo, hi)
            if lo > hi or lo > right or hi < left:
                return 0
            if left <= lo and hi <= right:
                return tr[idx]
            md = (lo + hi) // 2
            lsum = get_sum(2 * idx, lo, md, left, right)
            rsum = get_sum(2 * idx + 1, md + 1, hi, left, right)
            return lsum + rsum

        construct(1, 0, n - 1)
        for q in queries:
            tp, x, y = q
            if tp == 1:
                range_flip(1, 0, n - 1, x, y)
            elif tp == 2:
                sm = get_sum(1, 0, n - 1, 0, n - 1)
                cur_total += sm * x
            else:
                res.append(cur_total)
        return res
