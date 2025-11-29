class Solution:
    def confusingNumberII(self, n):
        if n < 1:
            return 0
        S = str(n)
        D = len(S)
        all_valid = [0, 1, 6, 8, 9]
        valid_first = [1, 6, 8, 9]
        center_digits = [0, 1, 8]
        rotate = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        # Count total valid digit numbers in [1, n]
        shorter_valid = 0
        p = 1
        for _ in range(D - 1):
            shorter_valid += 4 * p
            p *= 5
        same_valid = 0
        power = 5 ** (D - 1)
        prefix_ok = True
        for i in range(D):
            if not prefix_ok:
                break
            cd = int(S[i])
            lo = 1 if i == 0 else 0
            sm = sum(1 for v in all_valid if v >= lo and v < cd)
            same_valid += sm * power
            if cd not in rotate:
                prefix_ok = False
            power //= 5
        if prefix_ok:
            same_valid += 1
        total_valid = shorter_valid + same_valid

        # Generate all strobogrammatic numbers and count <= n
        strob = []
        def build(curr, half_len, is_odd):
            if len(curr) == half_len:
                if is_odd and curr[-1] not in center_digits:
                    return
                left = curr[:-1] if is_odd else curr
                mirr = [rotate[d] for d in reversed(left)]
                full = left + ([curr[-1]] if is_odd else []) + mirr
                num = 0
                for fd in full:
                    num = num * 10 + fd
                strob.append(num)
                return
            ch = valid_first if not curr else all_valid
            for d in ch:
                build(curr + [d], half_len, is_odd)
        for l in range(1, 11):
            hl = (l + 1) // 2
            is_o = l % 2 == 1
            build([], hl, is_o)
        strob_count = sum(1 for x in strob if x <= n)

        return total_valid - strob_count
