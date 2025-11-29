from sortedcontainers import SortedList
import collections

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__avails = SortedList([[0, a1]])
        self.__lookup = collections.defaultdict(list)

    def allocate(self, a1, a2):
        """
        """
        for v1, v2 in self.__avails:
            if v2 < a1:
                continue
            self.__avails.remove([v1, v2])
            self.__lookup[a2].append([v1, a1])
            if v2 - a1 > 0:
                self.__avails.add([v1 + a1, v2 - a1])
            return v1
        return -1

    def free(self, a1):
        """
        """
        if a1 not in self.__lookup:
            return 0
        v1 = 0
        for v2, v3 in self.__lookup[a1]:
            self.__avails.add([v2, v3])
            v4 = self.__avails.bisect_left([v2, v3])
            if v4 + 1 < len(self.__avails) and self.__avails[v4][0] + self.__avails[v4][1] == self.__avails[v4 + 1][0]:
                self.__avails[v4][1] += self.__avails[v4 + 1][1]
                del self.__avails[v4 + 1]
            if v4 - 1 >= 0 and self.__avails[v4 - 1][0] + self.__avails[v4 - 1][1] == self.__avails[v4][0]:
                self.__avails[v4 - 1][1] += self.__avails[v4][1]
                del self.__avails[v4]
            v1 += v3
        del self.__lookup[a1]
        return v1
