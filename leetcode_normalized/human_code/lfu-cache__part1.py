import collections

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__capa = a1
        self.__size = 0
        self.__min_freq = float('inf')
        self.__freq_to_nodes = collections.defaultdict(collections.OrderedDict)
        self.__key_to_freq = {}

    def get(self, a1):
        """
        """
        if a1 not in self.__key_to_freq:
            return -1
        v1 = self.__freq_to_nodes[self.__key_to_freq[a1]][a1]
        self.__update(a1, v1)
        return v1

    def put(self, a1, a2):
        """
        """
        if self.__capa <= 0:
            return
        if a1 not in self.__key_to_freq and self.__size == self.__capa:
            del self.__key_to_freq[self.__freq_to_nodes[self.__min_freq].popitem(last=False)[0]]
            if not self.__freq_to_nodes[self.__min_freq]:
                del self.__freq_to_nodes[self.__min_freq]
            self.__size -= 1
        self.__update(a1, a2)

    def __update(self, a1, a2):
        v1 = 0
        if a1 in self.__key_to_freq:
            v1 = self.__key_to_freq[a1]
            del self.__freq_to_nodes[v1][a1]
            if not self.__freq_to_nodes[v1]:
                del self.__freq_to_nodes[v1]
                if self.__min_freq == v1:
                    self.__min_freq += 1
            self.__size -= 1
        v1 += 1
        self.__min_freq = min(self.__min_freq, v1)
        self.__key_to_freq[a1] = v1
        self.__freq_to_nodes[v1][a1] = a2
        self.__size += 1
