import collections

class C1(object):

    def __init__(self):
        self.__nodes = set()
        self.__in_degree = collections.defaultdict(set)
        self.__out_degree = collections.defaultdict(set)

    def add_node(self, a1):
        self.__nodes.add(a1)

    def add_edge(self, a1, a2):
        (self.add_node(a1), self.add_node(a2))
        self.__in_degree[a2].add(a1)
        self.__out_degree[a1].add(a2)

    def sort(self):
        v1 = collections.deque()
        v2 = []
        for v3 in self.__nodes:
            if v3 not in self.__in_degree:
                v1.append(v3)
        while v1:
            v3 = v1.popleft()
            v2.append(v3)
            for v4 in self.__out_degree[v3]:
                self.__in_degree[v4].remove(v3)
                if not self.__in_degree[v4]:
                    self.__in_degree.pop(v4)
                    v1.append(v4)
        if len(v2) < len(self.__nodes):
            return
        return v2

class C2(object):

    def sortItems(self, a1, a2, a3, a4):
        """
        """
        for v1 in range(a1):
            if a3[v1] == -1:
                a3[v1] = a2
                a2 += 1
        v3 = C1()
        for v1 in range(a2):
            v3.add_node(v1)
        v4 = collections.defaultdict(C1)
        for v1 in range(a1):
            v4[a3[v1]].add_node(v1)
        for v1 in range(a1):
            for v5 in a4[v1]:
                if a3[v1] == a3[v5]:
                    v4[a3[v1]].add_edge(v5, v1)
                else:
                    v3.add_edge(a3[v5], a3[v1])
        v6 = []
        v7 = v3.sort()
        if v7 is None:
            return []
        for v1 in v7:
            v8 = v4[v1].sort()
            if v8 is None:
                return []
            for v9 in v8:
                v6.append(v9)
        return v6
