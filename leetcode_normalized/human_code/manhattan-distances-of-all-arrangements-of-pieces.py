v1 = 10 ** 9 + 7
v2, v3, v4 = [[1] * 2 for v5 in range(3)]

def f1(a1, a2):
    while len(v3) <= a1:
        v2.append(v2[-1] * len(v3) % v1)
        v3.append(v3[v1 % len(v3)] * (v1 - v1 // len(v3)) % v1)
        v4.append(v4[-1] * v3[-1] % v1)
    return v2[a1] * v4[a1 - a2] % v1 * v4[a2] % v1

class C1(object):

    def distanceSum(self, a1, a2, a3):
        """
        """

        def sum_n(a1):
            return (a1 + 1) * a1 // 2

        def sum_n_square(a1):
            return a1 * (a1 + 1) * (2 * a1 + 1) // 6

        def f(a1):
            return a1 * sum_n(a1 - 1) - sum_n_square(a1 - 1)
        return (f(a2) * a1 * a1 + f(a1) * a2 * a2) * f1(a1 * a2 - 2, a3 - 2) % v1
