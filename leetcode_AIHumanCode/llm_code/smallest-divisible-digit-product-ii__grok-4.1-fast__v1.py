class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def factorize(val: int) -> list[int]:
            if val < 2:
                return []
            exps = [0] * 4
            ps = [2, 3, 5, 7]
            for idx, p in enumerate(ps):
                while val % p == 0:
                    exps[idx] += 1
                    val //= p
            return exps if val == 1 else []

        req_exps = factorize(t)
        if not req_exps:
            return "-1"

        dig_exps = [[0] * 4 for _ in range(10)]
        for d in range(1, 10):
            dig_exps[d] = factorize(d)

        digits = [int(c) for c in num]
        n = len(digits)
        zpos = next((k for k in range(n) if digits[k] == 0), n)
        for k in range(zpos, n):
            digits[k] = 1

        total_exps = [0] * 4
        for d in digits:
            for j in range(4):
                total_exps[j] += dig_exps[d][j]

        if all(total_exps[j] >= req_exps[j] for j in range(4)):
            return ''.join(map(str, digits))

        def get_counts(needed: list[int]) -> list[int]:
            c2, c3, c5, c7 = needed
            counts = [0] * 8
            counts[6] = c2 // 3
            rem2 = c2 % 3
            counts[7] = c3 // 2
            rem3 = c3 % 2
            counts[3] = c5
            counts[5] = c7
            if rem2 == 2 and rem3 == 1:
                counts[0] = 1
                counts[4] = 1
            elif rem2 == 2:
                counts[2] = 1
            elif rem2 == 1 and rem3 == 1:
                counts[4] = 1
            elif rem2 == 1:
                counts[0] = 1
            elif rem3 == 1:
                counts[1] = 1
            return counts

        def make_suffix(dcounts: list[int], slen: int) -> str:
            nones = sum(dcounts)
            one_cnt = slen - nones
            parts = ['1'] * one_cnt
            for d in range(2, 10):
                parts.extend([str(d)] * dcounts[d - 2])
            return ''.join(parts)

        for p in range(n - 1, -1, -1):
            old_d = digits[p]
            for j in range(4):
                total_exps[j] -= dig_exps[old_d][j]
            for nd in range(old_d + 1, 10):
                temp_exps = [total_exps[j] + dig_exps[nd][j] for j in range(4)]
                rem_exps = [max(0, req_exps[j] - temp_exps[j]) for j in range(4)]
                d_cnts = get_counts(rem_exps)
                suf_sz = n - p - 1
                if sum(d_cnts) <= suf_sz:
                    suf = make_suffix(d_cnts, suf_sz)
                    return num[:p] + str(nd) + suf

        rem_exps = [max(0, req_exps[j] - total_exps[j]) for j in range(4)]
        d_cnts = get_counts(rem_exps)
        return make_suffix(d_cnts, n + 1)
