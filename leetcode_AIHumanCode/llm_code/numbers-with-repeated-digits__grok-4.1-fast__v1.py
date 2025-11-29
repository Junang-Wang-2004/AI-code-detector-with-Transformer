class Solution:
    def numDupDigitsAtMostN(self, N):
        s = str(N + 1)
        digs = [int(c) for c in s]
        length = len(digs)

        def perms(avail, need):
            res = 1
            for j in range(need):
                res *= avail - j
            return res

        cnt_unique = 0
        for sz in range(1, length):
            cnt_unique += 9 * perms(9, sz - 1)

        used = set()
        for pos in range(length):
            upper = digs[pos]
            start = 1 if pos == 0 else 0
            for cand in range(start, upper):
                if cand in used:
                    continue
                rem_pos = length - pos - 1
                avail_after = 10 - len(used) - 1
                cnt_unique += perms(avail_after, rem_pos)
            if upper in used:
                break
            used.add(upper)
        return N - cnt_unique
