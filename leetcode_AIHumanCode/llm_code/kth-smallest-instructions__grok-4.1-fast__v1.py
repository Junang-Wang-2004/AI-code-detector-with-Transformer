class Solution:
    def kthSmallestPath(self, destination, k):
        m, n = destination
        def binomial(p, q):
            if q == 0 or q == p:
                return 1
            q = min(q, p - q)
            frac = 1
            for i in range(q):
                frac = frac * (p - i) // (i + 1)
            return frac
        def construct_path(rem_v, rem_h, rem_k):
            if rem_v == 0 and rem_h == 0:
                return ''
            h_options = 0 if rem_h == 0 else binomial(rem_v + rem_h - 1, rem_v)
            if rem_k <= h_options:
                return 'H' + construct_path(rem_v, rem_h - 1, rem_k)
            else:
                return 'V' + construct_path(rem_v - 1, rem_h, rem_k - h_options)
        return construct_path(m, n, k)
