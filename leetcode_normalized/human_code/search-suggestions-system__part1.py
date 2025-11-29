import collections

class C1(object):

    def __init__(self):
        self.__TOP_COUNT = 3
        self.leaves = collections.defaultdict(C1)
        self.infos = []

    def insert(self, a1, a2):
        v1 = self
        for v2 in a1[a2]:
            v1 = v1.leaves[v2]
            v1.add_info(a1, a2)

    def add_info(self, a1, a2):
        self.infos.append(a2)
        self.infos.sort(key=lambda x: a1[x])
        if len(self.infos) > self.__TOP_COUNT:
            self.infos.pop()

class C2(object):

    def suggestedProducts(self, a1, a2):
        """
        """
        v1 = C1()
        for v2 in range(len(a1)):
            v1.insert(a1, v2)
        v3 = [[] for v4 in range(len(a2))]
        for v2, v5 in enumerate(a2):
            if v5 not in v1.leaves:
                break
            v1 = v1.leaves[v5]
            v3[v2] = [a1[x] for v6 in v1.infos]
        return v3
