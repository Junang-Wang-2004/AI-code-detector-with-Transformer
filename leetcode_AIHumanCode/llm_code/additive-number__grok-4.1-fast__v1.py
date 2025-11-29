class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)
        for p in range(1, n):
            if p > 1 and num[0] == '0':
                continue
            fst = int(num[:p])
            for q in range(p + 1, n):
                snd_str = num[p:q]
                if len(snd_str) > 1 and snd_str[0] == '0':
                    continue
                snd = int(snd_str)
                idx = q
                prv_a, prv_b = fst, snd
                ok = True
                while idx < n:
                    nxt = prv_a + prv_b
                    nxt_str = str(nxt)
                    nxt_l = len(nxt_str)
                    if idx + nxt_l > n or num[idx:idx + nxt_l] != nxt_str:
                        ok = False
                        break
                    idx += nxt_l
                    prv_a, prv_b = prv_b, nxt
                if ok and idx == n:
                    return True
        return False
