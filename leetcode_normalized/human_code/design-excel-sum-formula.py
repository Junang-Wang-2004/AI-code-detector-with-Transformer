import collections

class C1(object):

    def __init__(self, a1, a2):
        """
        """
        self.__exl = [[0 for v1 in range(ord(a2) - ord('A') + 1)] for v1 in range(a1 + 1)]
        self.__fward = collections.defaultdict(lambda: collections.defaultdict(int))
        self.__bward = collections.defaultdict(set)

    def set(self, a1, a2, a3):
        """
        """
        self.__reset_dependency(a1, a2)
        self.__update_others(a1, a2, a3)

    def get(self, a1, a2):
        """
        """
        return self.__exl[a1][ord(a2) - ord('A')]

    def sum(self, a1, a2, a3):
        """
        """
        self.__reset_dependency(a1, a2)
        v1 = self.__calc_and_update_dependency(a1, a2, a3)
        self.__update_others(a1, a2, v1)
        return v1

    def __reset_dependency(self, a1, a2):
        v1 = (a1, a2)
        if v1 in list(self.__bward.keys()):
            for v2 in self.__bward[v1]:
                self.__fward[v2].pop(v1, None)
            self.__bward[v1] = set()

    def __calc_and_update_dependency(self, a1, a2, a3):
        v1 = 0
        for v2 in a3:
            v2, v3 = (v2.split(':')[0], v2.split(':')[1] if ':' in v2 else v2)
            v4, v5, v6, v7 = (ord(v2[0]) - ord('A'), ord(v3[0]) - ord('A'), int(v2[1:]), int(v3[1:]))
            for v8 in range(v6, v7 + 1):
                for v9 in range(v4, v5 + 1):
                    v1 += self.__exl[v8][v9]
                    self.__fward[v8, chr(ord('A') + v9)][a1, a2] += 1
                    self.__bward[a1, a2].add((v8, chr(ord('A') + v9)))
        return v1

    def __update_others(self, a1, a2, a3):
        v1 = self.__exl[a1][ord(a2) - ord('A')]
        self.__exl[a1][ord(a2) - ord('A')] = a3
        v2 = collections.deque()
        v2.append(((a1, a2), a3 - v1))
        while v2:
            v3, v4 = v2.popleft()
            if v3 in self.__fward:
                for v5, v6 in self.__fward[v3].items():
                    v2.append((v5, v4 * v6))
                    self.__exl[v5[0]][ord(v5[1]) - ord('A')] += v4 * v6
