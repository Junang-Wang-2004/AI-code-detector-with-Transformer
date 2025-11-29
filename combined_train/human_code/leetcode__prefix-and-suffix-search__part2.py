class C1(object):

    def __init__(self):
        v1 = lambda: collections.defaultdict(v1)
        self.__trie = v1()

    def insert(self, a1, a2):

        def add_word(a1, a2):
            if '_words' not in a1:
                a1['_words'] = []
            a1['_words'].append(a2)
        v1 = self.__trie
        add_word(v1, a2)
        for v2 in a1:
            v1 = v1[v2]
            add_word(v1, a2)

    def find(self, a1):
        v1 = self.__trie
        for v2 in a1:
            if v2 not in v1:
                return []
            v1 = v1[v2]
        return v1['_words']

class C2(object):

    def __init__(self, a1):
        """
        """
        self.__prefix_trie = C1()
        self.__suffix_trie = C1()
        for v1 in reversed(range(len(a1))):
            self.__prefix_trie.insert(a1[v1], v1)
            self.__suffix_trie.insert(a1[v1][::-1], v1)

    def f(self, a1, a2):
        """
        """
        v1 = self.__prefix_trie.find(a1)
        v2 = self.__suffix_trie.find(a2[::-1])
        v3, v4 = (0, 0)
        while v3 != len(v1) and v4 != len(v2):
            if v1[v3] == v2[v4]:
                return v1[v3]
            elif v1[v3] > v2[v4]:
                v3 += 1
            else:
                v4 += 1
        return -1
