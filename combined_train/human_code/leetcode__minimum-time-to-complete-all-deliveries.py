class C1(object):

    def minimumTime(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1

        def lcm(a1, a2):
            return a1 // gcd(a1, a2) * a2

        def binary_search(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1

        def check(a1):
            return a1 - a1 // a2[0] >= a1[0] and a1 - a1 // a2[1] >= a1[1] and (a1 - a1 // l >= a1[0] + a1[1])
        v1 = lcm(a2[0], a2[1])
        return binary_search(sum(a1), sum(a1) * 2, check)
