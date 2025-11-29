import collections

class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))

    def find_set(self, a1):
        if self.set[a1] != a1:
            self.set[a1] = self.find_set(self.set[a1])
        return self.set[a1]

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 == v2:
            return False
        self.set[max(v1, v2)] = min(v1, v2)
        return True

class C2(object):

    def smallestStringWithSwaps(self, a1, a2):
        """
        """
        v1 = C1(len(a1))
        for v2, v3 in a2:
            v1.union_set(v2, v3)
        v4 = collections.defaultdict(list)
        for v5 in range(len(a1)):
            v4[v1.find_set(v5)].append(a1[v5])
        for v5 in v4.keys():
            v4[v5].sort(reverse=True)
        v6 = []
        for v5 in range(len(a1)):
            v6.append(v4[v1.find_set(v5)].pop())
        return ''.join(v6)
