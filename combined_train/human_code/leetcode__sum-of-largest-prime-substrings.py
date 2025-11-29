import random

class C1(object):

    def sumOfLargestPrimes(self, a1):
        """
        """
        v1 = 3

        def nth_element(a1, a2, a3=0, a4=lambda a, b: a < b):

            def tri_partition(a1, a2, a3, a4, a5):
                v1 = a2
                while v1 <= a3:
                    if a1[v1] == a4:
                        v1 += 1
                    elif a5(a1[v1], a4):
                        a1[a2], a1[v1] = (a1[v1], a1[a2])
                        a2 += 1
                        v1 += 1
                    else:
                        a1[v1], a1[a3] = (a1[a3], a1[v1])
                        a3 -= 1
                return (a2, a3)
            v1 = len(a1) - 1
            while a3 <= v1:
                v2 = random.randint(a3, v1)
                v3, v4 = tri_partition(a1, a3, v1, a1[v2], a4)
                if v3 <= a2 <= v4:
                    return
                elif v3 > a2:
                    v1 = v3 - 1
                else:
                    a3 = v4 + 1

        def is_prime(a1):
            if a1 == 1:
                return False
            if a1 in (2, 3):
                return True
            if a1 % 2 == 0 or a1 % 3 == 0:
                return False
            for v1 in range(5, a1, 6):
                if v1 * v1 > a1:
                    break
                if a1 % v1 == 0 or a1 % (v1 + 2) == 0:
                    return False
            return True
        v2 = set()
        for v3 in range(len(a1)):
            v4 = 0
            for v5 in range(v3, len(a1)):
                v4 = v4 * 10 + int(a1[v5])
                if is_prime(v4):
                    v2.add(v4)
        v6 = list(v2)
        v7 = min(len(v6), v1)
        nth_element(v6, v7, compare=lambda a, b: a > b)
        return sum((v6[v3] for v3 in range(v7)))
