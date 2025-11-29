class C1(object):

    def findKthSmallest(self, a1, a2):
        """
        """

        def popcount(a1):
            return bin(a1).count('1')

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1

        def lcm(a1, a2):
            return a1 // gcd(a1, a2) * a2

        def check(a1):
            return sum(((-1 if i + 1 & 1 else +1) * (a1 // l) for v1 in range(1, len(a1) + 1) for v2 in lookup[v1])) >= a2

        def binary_search(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3 in range(1, 1 << len(a1)):
            v1[popcount(v3)].append(reduce(lcm, (a1[i] for v4 in range(len(a1)) if v3 & 1 << v4)))
        v5 = min(a1)
        return binary_search(v5, a2 * v5, check)
