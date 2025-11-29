from collections import defaultdict

class C1(object):
    v1 = {}

    def chain_length(self, a1):
        if a1 in self.cache:
            return self.cache[a1]
        v1 = 0
        v2 = a1
        while v2 > 1:
            if v2 in self.cache:
                v1 += self.cache[v2]
                break
            v1 += 1
            v2 = v2 // 2 if v2 % 2 == 0 else 3 * v2 + 1
        self.cache[a1] = v1
        return v1

    def getKth(self, a1, a2, a3):
        v1 = defaultdict(list)
        for v2 in range(a1, a2 + 1):
            v3 = self.chain_length(v2)
            v1[v3].append(v2)
        v4 = sorted(v1)
        v5 = 0
        for v3 in v4:
            v6 = v1[v3]
            v7 = len(v6)
            if v5 + v7 >= a3:
                return v6[a3 - v5 - 1]
            v5 += v7
