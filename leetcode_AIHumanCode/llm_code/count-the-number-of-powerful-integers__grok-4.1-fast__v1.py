class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        def count_valid(bound):
            if bound < 0:
                return 0
            sbound = str(bound)
            ks = len(s)
            prefix_s = sbound[:-ks]
            suffix_s = sbound[-ks:]
            tgt = int(s)
            suf_val = int(suffix_s)
            plen = len(prefix_s)
            res = 0
            opts = limit + 1
            mult = pow(opts, plen)
            for p in range(plen):
                mult //= opts
                dval = int(prefix_s[p])
                lo_choices = min(dval - 1, limit) + 1
                res += lo_choices * mult
                if dval > limit:
                    break
            else:
                if suf_val >= tgt:
                    res += 1
            return res

        return count_valid(finish) - count_valid(start - 1)
