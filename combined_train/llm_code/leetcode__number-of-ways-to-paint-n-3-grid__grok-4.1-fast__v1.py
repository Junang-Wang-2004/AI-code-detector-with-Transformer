class C1(object):

    def numOfWays(self, a1):
        v1 = 10 ** 9 + 7

        def mult(a1, a2):
            return [[(a1[0][0] * a2[0][0] + a1[0][1] * a2[1][0]) % v1, (a1[0][0] * a2[0][1] + a1[0][1] * a2[1][1]) % v1], [(a1[1][0] * a2[0][0] + a1[1][1] * a2[1][0]) % v1, (a1[1][0] * a2[0][1] + a1[1][1] * a2[1][1]) % v1]]

        def power(a1, a2):
            v1 = [[1, 0], [0, 1]]
            while a2 > 0:
                if a2 & 1:
                    v1 = mult(v1, a1)
                a1 = mult(a1, a1)
                a2 >>= 1
            return v1
        v2 = [[3, 2], [2, 2]]
        if a1 == 0:
            return 0
        v3 = power(v2, a1 - 1)
        v4 = (6 * v3[0][0] + 6 * v3[1][0]) % v1
        v5 = (6 * v3[0][1] + 6 * v3[1][1]) % v1
        return (v4 + v5) % v1
