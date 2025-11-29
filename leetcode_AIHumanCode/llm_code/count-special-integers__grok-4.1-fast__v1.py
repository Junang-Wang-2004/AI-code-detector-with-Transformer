class Solution:
    def countSpecialNumbers(self, n):
        if n == 0:
            return 0
        s = str(n)
        digs = [int(c) for c in s]
        length = len(digs)
        total = 0
        for sz in range(1, length):
            cnt = 9
            for pos in range(1, sz):
                cnt *= 10 - pos
            total += cnt
        forbidden = set()
        for idx in range(length):
            lo = 1 if idx == 0 else 0
            hi = digs[idx]
            for choice in range(lo, hi):
                if choice in forbidden:
                    continue
                remaining_slots = length - idx - 1
                free_digits = 10 - len(forbidden) - 1
                if free_digits < remaining_slots:
                    continue
                ways = 1
                for step in range(remaining_slots):
                    ways *= free_digits - step
                total += ways
            this_digit = digs[idx]
            if this_digit in forbidden:
                break
            forbidden.add(this_digit)
        else:
            total += 1
        return total
