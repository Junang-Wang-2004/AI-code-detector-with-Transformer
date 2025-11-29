import itertools

class C1(object):

    def minimumCost(self, a1, a2, a3):
        """
        """
        v1 = float('inf')

        class Trie(object):

            def __init__(self):
                self.__nodes = []
                self.__mns = []
                self.__new_node()

            def __new_node(self):
                self.__nodes.append([-1] * 26)
                self.__mns.append(v1)
                return len(self.__nodes) - 1

            def add(self, a1, a2):
                v1 = 0
                for v2 in a1:
                    v2 = ord(v2) - ord('a')
                    if self.__nodes[v1][v2] == -1:
                        self.__nodes[v1][v2] = self.__new_node()
                    v1 = self.__nodes[v1][v2]
                self.__mns[v1] = min(self.__mns[v1], a2)

            def query(self, a1):
                v1 = 0
                for v2 in range(a1, len(a1)):
                    v3 = ord(a1[v2]) - ord('a')
                    if self.__nodes[v1][v3] == -1:
                        break
                    v1 = self.__nodes[v1][v3]
                    if self.__mns[v1] != v1:
                        dp[v2 + 1] = min(dp[v2 + 1], dp[a1] + self.__mns[v1])
        v2 = Trie()
        for v3, v4 in zip(a2, a3):
            v2.add(v3, v4)
        v5 = [v1] * (len(a1) + 1)
        v5[0] = 0
        for v6 in range(len(a1)):
            if v5[v6] == v1:
                continue
            v2.query(v6)
        return v5[-1] if v5[-1] != v1 else -1
