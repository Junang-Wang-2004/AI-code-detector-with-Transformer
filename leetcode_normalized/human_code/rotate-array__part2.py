from fractions import gcd

class C1(object):
    """
    """

    def rotate(self, a1, a2):

        def apply_cycle_permutation(a1, a2, a3, a4):
            v1 = a4[a2]
            for v2 in range(1, a3):
                a4[(a2 + v2 * a1) % len(a4)], v1 = (v1, a4[(a2 + v2 * a1) % len(a4)])
            a4[a2] = v1
        a2 %= len(a1)
        v2 = gcd(len(a1), a2)
        v3 = len(a1) / v2
        for v4 in range(v2):
            apply_cycle_permutation(a2, v4, v3, a1)
