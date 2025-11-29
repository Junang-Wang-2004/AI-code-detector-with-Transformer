import math
import random

class C1:
    v1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def is_prime(self, a1):
        v1 = self.is_prime_common(a1)
        if v1 is not None:
            return v1
        if a1 < 2000000:
            return self.is_prime_brute_force(a1)
        return self.is_prime_miller_rabin(a1)

    def is_prime_common(self, a1):
        if a1 == 1:
            return False
        if a1 in C1.seed_primes:
            return True
        if any(map(lambda x: a1 % x == 0, self.seed_primes)):
            return False

    def is_prime_brute_force(self, a1):
        for v1 in range(2, int(math.sqrt(a1)) + 1):
            if a1 % v1 == 0:
                return False
        return True

    def is_prime_miller_rabin(self, a1):
        v1 = a1 - 1
        while v1 & 1 == 0:
            v1 >>= 1
        v2 = self.get_witnesses(a1)
        for v3 in v2:
            v4 = pow(v3, v1, a1)
            while v1 != a1 - 1 and v4 != 1 and (v4 != a1 - 1):
                v4 = v4 * v4 % a1
                v1 <<= 1
            if v4 != a1 - 1 and v1 & 1 == 0:
                return False
        return True

    def get_witnesses(self, a1):

        def _get_range(a1):
            if a1 < 2047:
                return 1
            if a1 < 1373653:
                return 2
            if a1 < 25326001:
                return 3
            if a1 < 3215031751:
                return 4
            if a1 < 2152302898747:
                return 5
            if a1 < 3474749660383:
                return 6
            if a1 < 341550071728321:
                return 7
            if a1 < 3825123056546413051:
                return 9
            return 12
        return self.seed_primes[:_get_range(a1)]

    def gcd(self, a1, a2):
        if a1 < a2:
            return self.gcd(a2, a1)
        if a2 == 0:
            return a1
        while a2:
            a1, a2 = (a2, a1 % a2)
        return a1

    @staticmethod
    def f(a1, a2, a3):
        v1 = C1.seed_primes[a3 % len(C1.seed_primes)]
        return (v1 * a1 + a3) % a2

    def find_factor(self, a1, a2=1):
        if self.is_prime(a1):
            return a1
        v1, v2, v3 = (2, 2, 1)
        v4 = 0
        while v3 == 1:
            v4 += 1
            v1 = self.f(v1, a1, a2)
            v2 = self.f(self.f(v2, a1, a2), a1, a2)
            v3 = self.gcd(abs(v1 - v2), a1)
        if v3 == a1:
            return self.find_factor(a1, a2 + 1)
        return self.find_factor(v3)

    def find_factors(self, a1):
        v1 = {}
        if self.is_prime(a1):
            v1[a1] = 1
            return v1
        while a1 > 1:
            v2 = self.find_factor(a1)
            v1.setdefault(v2, 0)
            v1[v2] += 1
            a1 //= v2
        return v1

class C2:

    def __init__(self, a1, a2):
        self.f = [1]
        for v1 in range(1, a1 + 1):
            self.f.append(self.f[-1] * v1 % a2)
        self.i = [pow(self.f[-1], a2 - 2, a2)]
        for v1 in range(1, a1 + 1)[::-1]:
            self.i.append(self.i[-1] * v1 % a2)
        self.i.reverse()

    def factorial(self, a1):
        return self.f[a1]

    def ifactorial(self, a1):
        return self.i[a1]

    def comb(self, a1, a2):
        return self.f[a1] * self.i[a1 - a2] % mod * self.i[a2] % mod
v1 = 10 ** 9 + 7
v2, v3 = map(int, input().split())
*v4, = C1().find_factors(v3).values()
if v4:
    v5 = C2(v2 + max(v4), v1)
v6 = 1
for v7 in v4:
    v6 = v6 * v5.comb(v2 - 1 + v7, v7) % v1
print(v6)
