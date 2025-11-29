import collections

class C1(object):

    def __init__(self, a1):
        """
        """
        v1 = lambda: collections.defaultdict(v1)
        self.__trie = v1()
        for v2, v3 in enumerate(a1):
            v3 += '#'
            for v4 in range(len(v3)):
                v5 = self.__trie
                v5['_weight'] = v2
                for v6 in range(v4, 2 * len(v3) - 1):
                    v5 = v5[v3[v6 % len(v3)]]
                    v5['_weight'] = v2

    def f(self, a1, a2):
        """
        """
        v1 = self.__trie
        for v2 in a2 + '#' + a1:
            if v2 not in v1:
                return -1
            v1 = v1[v2]
        return v1['_weight']
