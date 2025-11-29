from sortedcontainers import SortedList

class C1(object):

    def __init__(self):
        self.__idx_to_num = {}
        self.__num_to_idxs = collections.defaultdict(SortedList)

    def change(self, a1, a2):
        """
        """
        if a1 in self.__idx_to_num:
            self.__num_to_idxs[self.__idx_to_num[a1]].remove(a1)
            if not self.__num_to_idxs[self.__idx_to_num[a1]]:
                del self.__num_to_idxs[self.__idx_to_num[a1]]
        self.__idx_to_num[a1] = a2
        self.__num_to_idxs[a2].add(a1)

    def find(self, a1):
        """
        """
        return self.__num_to_idxs[a1][0] if a1 in self.__num_to_idxs else -1
