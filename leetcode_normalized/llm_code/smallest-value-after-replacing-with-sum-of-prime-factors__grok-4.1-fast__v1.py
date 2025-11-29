class C1:

    def smallestValue(self, a1):

        def factor_sum(a1):
            v1 = 0
            while a1 % 2 == 0:
                v1 += 2
                a1 //= 2
            v3 = 3
            while v3 * v3 <= a1:
                while a1 % v3 == 0:
                    v1 += v3
                    a1 //= v3
                v3 += 2
            if a1 > 1:
                v1 += a1
            return v1
        while True:
            v1 = factor_sum(a1)
            if v1 == a1:
                return a1
            a1 = v1
