from collections import defaultdict

class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))
        self.rank = [0] * a1
        self.comp_size = [1] * a1

    def get_root(self, a1):
        if self.parent[a1] != a1:
            self.parent[a1] = self.get_root(self.parent[a1])
        return self.parent[a1]

    def merge(self, a1, a2):
        v1, v2 = (self.get_root(a1), self.get_root(a2))
        if v1 == v2:
            return
        if self.rank[v1] < self.rank[v2]:
            self.parent[v1] = v2
            self.comp_size[v2] += self.comp_size[v1]
        elif self.rank[v1] > self.rank[v2]:
            self.parent[v2] = v1
            self.comp_size[v1] += self.comp_size[v2]
        else:
            self.parent[v2] = v1
            self.comp_size[v1] += self.comp_size[v2]
            self.rank[v1] += 1

class C2:

    def largestComponentSize(self, a1):

        def extract_primes(a1):
            v1 = []
            if a1 < 2:
                return v1
            while a1 % 2 == 0:
                v1.append(2)
                a1 //= 2
                break
            v3 = 3
            while v3 * v3 <= a1:
                if a1 % v3 == 0:
                    v1.append(v3)
                    while a1 % v3 == 0:
                        a1 //= v3
                v3 += 2
            if a1 > 1:
                v1.append(a1)
            return v1
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = C1(v1)
        v3 = defaultdict(list)
        for v4, v5 in enumerate(a1):
            for v6 in extract_primes(v5):
                v3[v6].append(v4)
        for v7 in v3.values():
            v8 = v7[0]
            for v9 in v7[1:]:
                v2.merge(v8, v9)
        v10 = max((v2.comp_size[v2.get_root(i)] for v11 in range(v1)))
        return v10
