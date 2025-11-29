import collections

class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.size = [1] * a1

    def find_set(self, a1):
        if self.set[a1] != a1:
            self.set[a1] = self.find_set(self.set[a1])
        return self.set[a1]

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 == v2:
            return False
        self.set[min(v1, v2)] = max(v1, v2)
        self.size[max(v1, v2)] += self.size[min(v1, v2)]
        return True

class C2(object):

    def largestComponentSize(self, a1):
        """
        """

        def prime_factors(a1):
            v1 = []
            v2 = 2
            if a1 % v2 == 0:
                while a1 % v2 == 0:
                    a1 //= v2
                v1.append(v2)
            v2 = 3
            while v2 * v2 <= a1:
                if a1 % v2 == 0:
                    while a1 % v2 == 0:
                        a1 //= v2
                    v1.append(v2)
                v2 += 2
            if a1 != 1:
                v1.append(a1)
            return v1
        v1 = C1(len(a1))
        v2 = collections.defaultdict(int)
        for v3 in range(len(a1)):
            for v4 in prime_factors(a1[v3]):
                if v4 not in v2:
                    v2[v4] = v3
                v1.union_set(v2[v4], v3)
        return max(v1.size)
