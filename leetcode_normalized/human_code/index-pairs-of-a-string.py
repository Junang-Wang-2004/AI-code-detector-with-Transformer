import collections

class C1(object):

    def __init__(self):
        self.children = collections.defaultdict(C1)
        self.indices = []
        self.suffix = None
        self.output = None

class C2(object):

    def step(self, a1):
        while self.__node and a1 not in self.__node.children:
            self.__node = self.__node.suffix
        self.__node = self.__node.children[a1] if self.__node else self.__root
        return self.__get_ac_node_outputs(self.__node)

    def __init__(self, a1):
        self.__root = self.__create_ac_trie(a1)
        self.__node = self.__create_ac_suffix_and_output_links(self.__root)

    def __create_ac_trie(self, a1):
        v1 = C1()
        for v2, v3 in enumerate(a1):
            v4 = v1
            for v5 in v3:
                v4 = v4.children[v5]
            v4.indices.append(v2)
        return v1

    def __create_ac_suffix_and_output_links(self, a1):
        v1 = collections.deque()
        for v2 in a1.children.values():
            v1.append(v2)
            v2.suffix = a1
        while v1:
            v2 = v1.popleft()
            for v3, v4 in v2.children.items():
                v1.append(v4)
                v5 = v2.suffix
                while v5 and v3 not in v5.children:
                    v5 = v5.suffix
                v4.suffix = v5.children[v3] if v5 else a1
                v4.output = v4.suffix if v4.suffix.indices else v4.suffix.output
        return a1

    def __get_ac_node_outputs(self, a1):
        v1 = []
        for v2 in a1.indices:
            v1.append(v2)
        v3 = a1.output
        while v3:
            for v2 in v3.indices:
                v1.append(v2)
            v3 = v3.output
        return v1

class C3(object):

    def indexPairs(self, a1, a2):
        """
        """
        v1 = []
        v2 = [w[::-1] for v3 in a2]
        v4 = C2(v2)
        for v5 in reversed(range(len(a1))):
            for v6 in v4.step(a1[v5]):
                v1.append([v5, v5 + len(v2[v6]) - 1])
        v1.reverse()
        return v1
