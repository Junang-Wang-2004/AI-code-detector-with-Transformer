import itertools

class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.rank = [0] * a1

    def find_set(self, a1):
        v1 = []
        while self.set[a1] != a1:
            v1.append(a1)
            a1 = self.set[a1]
        while v1:
            self.set[v1.pop()] = a1
        return a1

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 == v2:
            return False
        if self.rank[v1] < self.rank[v2]:
            self.set[v1] = v2
        elif self.rank[v1] > self.rank[v2]:
            self.set[v2] = v1
        else:
            self.set[v2] = v1
            self.rank[v1] += 1
        return True

class C2(object):

    def gcdSort(self, a1):
        """
        """

        def modified_sieve_of_eratosthenes(a1, a2, a3):
            if a1 < 2:
                return
            v1 = [True] * (a1 + 1)
            for v2 in range(2, len(v1)):
                if not v1[v2]:
                    continue
                for v3 in range(v2 + v2, len(v1), v2):
                    v1[v3] = False
                    if v3 in a2:
                        a3.union_set(v2 - 1, v3 - 1)
        v1 = max(a1)
        v2 = C1(v1)
        modified_sieve_of_eratosthenes(v1, set(a1), v2)
        return all((v2.find_set(a - 1) == v2.find_set(b - 1) for v3, v4 in zip(a1, sorted(a1))))
