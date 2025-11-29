import collections

class C1(object):

    def __init__(self, a1):
        self.cache = collections.OrderedDict()
        self.capacity = a1

    def get(self, a1):
        if a1 not in self.cache:
            return -1
        v1 = self.cache[a1]
        self.__update(a1, v1)
        return v1

    def put(self, a1, a2):
        if a1 not in self.cache and len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.__update(a1, a2)

    def __update(self, a1, a2):
        if a1 in self.cache:
            del self.cache[a1]
        self.cache[a1] = a2
