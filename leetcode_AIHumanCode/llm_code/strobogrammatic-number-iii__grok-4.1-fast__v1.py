class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        rev_map = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        memo = {}
        max_l = max(len(low), len(high))
        len_stro = [0] * (max_l + 1)
        if max_l >= 1:
            len_stro[1] = 3
        if max_l >= 2:
            len_stro[2] = 4
        if max_l >= 3:
            len_stro[3] = 12
        for i in range(4, max_l + 1):
            len_stro[i] = 5 * len_stro[i - 2]
        pref_stro = [0] * (max_l + 2)
        for i in range(1, max_l + 1):
            pref_stro[i] = pref_stro[i - 1] + len_stro[i]

        def valid_stro(s: str) -> bool:
            sl = len(s)
            for p in range(sl // 2 + 1):
                q = sl - 1 - p
                if s[q] not in rev_map or s[p] != rev_map[s[q]]:
                    return False
            return True

        def tally_leq(num_str: str, leadz_ok: bool) -> int:
            ckey = (num_str, leadz_ok)
            if ckey in memo:
                return memo[ckey]
            res = 0
            ln = len(num_str)
            if not leadz_ok:
                res = pref_stro[ln - 1]
            if ln == 1:
                for dc in '018':
                    if num_str >= dc:
                        res += 1
            else:
                for fst_d, lst_d in rev_map.items():
                    if not leadz_ok and fst_d == '0':
                        continue
                    if num_str[0] > fst_d:
                        m_sz = ln - 2
                        if m_sz == 0:
                            res += 1
                        else:
                            res += tally_leq('9' * m_sz, True)
                    elif num_str[0] == fst_d:
                        if ln == 2:
                            if num_str[-1] >= lst_d:
                                res += 1
                        else:
                            md_str = num_str[1:-1]
                            md_ln = ln - 2
                            if num_str[-1] >= lst_d:
                                res += tally_leq(md_str, True)
                            elif md_str != '0' * md_ln:
                                res += tally_leq(md_str, True) - (1 if valid_stro(md_str) else 0)
            memo[ckey] = res
            return res

        ch = tally_leq(high, False)
        cl = tally_leq(low, False)
        return ch - cl + (1 if valid_stro(low) else 0)
