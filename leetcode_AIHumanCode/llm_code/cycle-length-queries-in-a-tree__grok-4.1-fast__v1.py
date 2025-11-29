class Solution:
    def cycleLengthQueries(self, n, queries):
        res = []
        for u, v in queries:
            du = u.bit_length() - 1
            dv = v.bit_length() - 1
            ou, ov = du, dv
            if du > dv:
                u >>= du - dv
                cd = dv
            elif dv > du:
                v >>= dv - du
                cd = du
            else:
                cd = du
            xo = u ^ v
            sh = xo.bit_length()
            dl = cd - sh
            res.append(ou + ov - 2 * dl + 1)
        return res
