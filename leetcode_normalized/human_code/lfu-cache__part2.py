import collections

class C1(object):

    def __init__(self, a1, a2, a3):
        self.key = a1
        self.val = a2
        self.freq = a3
        self.next = None
        self.prev = None

class C2(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, a1):
        a1.next, a1.prev = (None, None)
        if self.head is None:
            self.head = a1
        else:
            self.tail.next = a1
            a1.prev = self.tail
        self.tail = a1

    def delete(self, a1):
        if a1.prev:
            a1.prev.next = a1.__next__
        else:
            self.head = a1.__next__
        if a1.__next__:
            a1.next.prev = a1.prev
        else:
            self.tail = a1.prev
        a1.next, a1.prev = (None, None)

class C3(object):

    def __init__(self, a1):
        """
        """
        self.__capa = a1
        self.__size = 0
        self.__min_freq = float('inf')
        self.__freq_to_nodes = collections.defaultdict(C2)
        self.__key_to_node = {}

    def get(self, a1):
        """
        """
        if a1 not in self.__key_to_node:
            return -1
        v1 = self.__key_to_node[a1].val
        self.__update(a1, v1)
        return v1

    def put(self, a1, a2):
        """
        """
        if self.__capa <= 0:
            return
        if a1 not in self.__key_to_node and self.__size == self.__capa:
            del self.__key_to_node[self.__freq_to_nodes[self.__min_freq].head.key]
            self.__freq_to_nodes[self.__min_freq].delete(self.__freq_to_nodes[self.__min_freq].head)
            if not self.__freq_to_nodes[self.__min_freq].head:
                del self.__freq_to_nodes[self.__min_freq]
            self.__size -= 1
        self.__update(a1, a2)

    def __update(self, a1, a2):
        v1 = 0
        if a1 in self.__key_to_node:
            v2 = self.__key_to_node[a1]
            v1 = v2.freq
            self.__freq_to_nodes[v1].delete(v2)
            if not self.__freq_to_nodes[v1].head:
                del self.__freq_to_nodes[v1]
                if self.__min_freq == v1:
                    self.__min_freq += 1
            self.__size -= 1
        v1 += 1
        self.__min_freq = min(self.__min_freq, v1)
        self.__key_to_node[a1] = C1(a1, a2, v1)
        self.__freq_to_nodes[v1].append(self.__key_to_node[a1])
        self.__size += 1
