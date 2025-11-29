class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.rank = [0] * a1
        self.size = [1] * a1

    def find_set(self, a1):
        v1 = []
        while self.set[a1] != a1:
            v1.append(a1)
            a1 = self.set[a1]
        while v1:
            self.set[v1.pop()] = a1
        return a1

    def union_set(self, a1, a2):
        a1, a2 = (self.find_set(a1), self.find_set(a2))
        if a1 == a2:
            return False
        if self.rank[a1] > self.rank[a2]:
            a1, a2 = (a2, a1)
        self.set[a1] = self.set[a2]
        if self.rank[a1] == self.rank[a2]:
            self.rank[a2] += 1
        self.size[a2] += self.size[a1]
        return True

    def total(self, a1):
        return self.size[self.find_set(a1)]

class C2(object):

    def countPaths(self, a1, a2):
        """
        """

        def linear_sieve_of_eratosthenes(a1):
            v1 = []
            v2 = [-1] * (a1 + 1)
            for v3 in range(2, a1 + 1):
                if v2[v3] == -1:
                    v2[v3] = v3
                    v1.append(v3)
                for v4 in v1:
                    if v3 * v4 > a1 or v4 > v2[v3]:
                        break
                    v2[v3 * v4] = v4
            return v2

        def is_prime(a1):
            return spf[a1] == a1
        v1 = linear_sieve_of_eratosthenes(a1)
        v2 = C1(a1)
        for v3, v4 in a2:
            v3, v4 = (v3 - 1, v4 - 1)
            if is_prime(v3 + 1) == is_prime(v4 + 1) == False:
                v2.union_set(v3, v4)
        v5 = 0
        v6 = [1] * a1
        for v3, v4 in a2:
            v3, v4 = (v3 - 1, v4 - 1)
            if is_prime(v3 + 1) == is_prime(v4 + 1):
                continue
            if not is_prime(v3 + 1):
                v3, v4 = (v4, v3)
            v5 += v6[v3] * v2.total(v4)
            v6[v3] += v2.total(v4)
        return v5
