import collections

class C1(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__idx_to_val = collections.defaultdict(int)
        self.__val_to_idxs = collections.defaultdict(list)
        self.__top = None
        self.__max = None

    def push(self, a1):
        """
        """
        v1 = self.__val_to_idxs[self.__top][-1] + 1 if self.__val_to_idxs else 0
        self.__idx_to_val[v1] = a1
        self.__val_to_idxs[a1].append(v1)
        self.__top = a1
        self.__max = max(self.__max, a1)

    def pop(self):
        """
        """
        v1 = self.__top
        self.__remove(v1)
        return v1

    def top(self):
        """
        """
        return self.__top

    def peekMax(self):
        """
        """
        return self.__max

    def popMax(self):
        """
        """
        v1 = self.__max
        self.__remove(v1)
        return v1

    def __remove(self, a1):
        v1 = self.__val_to_idxs[a1][-1]
        self.__val_to_idxs[a1].pop()
        if not self.__val_to_idxs[a1]:
            del self.__val_to_idxs[a1]
        del self.__idx_to_val[v1]
        if a1 == self.__top:
            self.__top = self.__idx_to_val[max(self.__idx_to_val.keys())] if self.__idx_to_val else None
        if a1 == self.__max:
            self.__max = max(self.__val_to_idxs.keys()) if self.__val_to_idxs else None
