class Solution(object):
    def findProductsOfElements(self, queries):
        def ones_up_to(n):
            if n < 0:
                return 0
            res = 0
            pos = 0
            while (1 << pos) <= n:
                cycle = 1 << (pos + 1)
                full = (n + 1) // cycle
                res += full * (cycle // 2)
                rem = (n + 1) % cycle
                if rem > (1 << pos):
                    res += rem - (1 << pos)
                pos += 1
            return res

        def sum_pos_up_to(n):
            if n < 0:
                return 0
            res = 0
            pos = 0
            while (1 << pos) <= n:
                cycle = 1 << (pos + 1)
                full = (n + 1) // cycle
                cnt = full * (cycle // 2)
                rem = (n + 1) % cycle
                if rem > (1 << pos):
                    cnt += rem - (1 << pos)
                res += pos * cnt
                pos += 1
            return res

        def find_smallest_y(tgt):
            lo = 0
            hi = tgt
            while lo < hi:
                md = lo + (hi - lo) // 2
                if ones_up_to(md) >= tgt:
                    hi = md
                else:
                    lo = md + 1
            return lo

        def total_pos_sum(tgt):
            if tgt == 0:
                return 0
            y = find_smallest_y(tgt)
            prev_ones = ones_up_to(y - 1)
            prev_sum = sum_pos_up_to(y - 1)
            rem = tgt - prev_ones
            extra_sum = 0
            bitpos = 0
            y_bits = y
            while rem > 0 and (1 << bitpos) <= y_bits:
                if y_bits & (1 << bitpos):
                    extra_sum += bitpos
                    rem -= 1
                bitpos += 1
            return prev_sum + extra_sum

        return [pow(2, total_pos_sum(r + 1) - total_pos_sum(l), m) for l, r, m in queries]
