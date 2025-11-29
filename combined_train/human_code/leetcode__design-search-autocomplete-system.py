import collections

class C1(object):

    def __init__(self):
        self.__TOP_COUNT = 3
        self.infos = []
        self.leaves = {}

    def insert(self, a1, a2):
        v1 = self
        v1.add_info(a1, a2)
        for v2 in a1:
            if v2 not in v1.leaves:
                v1.leaves[v2] = C1()
            v1 = v1.leaves[v2]
            v1.add_info(a1, a2)

    def add_info(self, a1, a2):
        for v1 in self.infos:
            if v1[1] == a1:
                v1[0] = -a2
                break
        else:
            self.infos.append([-a2, a1])
        self.infos.sort()
        if len(self.infos) > self.__TOP_COUNT:
            self.infos.pop()

class C2(object):

    def __init__(self, a1, a2):
        """
        """
        self.__trie = C1()
        self.__cur_node = self.__trie
        self.__search = []
        self.__sentence_to_count = collections.defaultdict(int)
        for v1, v2 in zip(a1, a2):
            self.__sentence_to_count[v1] = v2
            self.__trie.insert(v1, v2)

    def input(self, a1):
        """
        """
        v1 = []
        if a1 == '#':
            self.__sentence_to_count[''.join(self.__search)] += 1
            self.__trie.insert(''.join(self.__search), self.__sentence_to_count[''.join(self.__search)])
            self.__cur_node = self.__trie
            self.__search = []
        else:
            self.__search.append(a1)
            if self.__cur_node:
                if a1 not in self.__cur_node.leaves:
                    self.__cur_node = None
                    return []
                self.__cur_node = self.__cur_node.leaves[a1]
                v1 = [p[1] for v2 in self.__cur_node.infos]
        return v1
