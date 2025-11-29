class C1:

    def sumOfLargestPrimes(self, a1):

        def check_prime(a1):
            if a1 <= 1:
                return False
            if a1 <= 3:
                return True
            if a1 % 2 == 0 or a1 % 3 == 0:
                return False
            v1 = 5
            while v1 * v1 <= a1:
                if a1 % v1 == 0 or a1 % (v1 + 2) == 0:
                    return False
                v1 += 6
            return True
        v1 = set()
        v2 = len(a1)
        for v3 in range(1, v2 + 1):
            for v4 in range(v2 - v3 + 1):
                v5 = a1[v4:v4 + v3]
                v6 = int(v5)
                if v6 > 1 and check_prime(v6):
                    v1.add(v6)
        v7 = sorted(v1, reverse=True)
        v8 = min(3, len(v7))
        return sum(v7[:v8])
