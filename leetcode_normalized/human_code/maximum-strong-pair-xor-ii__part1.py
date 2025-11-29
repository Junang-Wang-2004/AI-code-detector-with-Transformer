class C1(object):

    def maximumStrongPairXor(self, a1):
        """
        """

        class Trie(object):

            def __init__(self, a1):
                self.__nodes = []
                self.__cnts = []
                self.__new_node()
                self.__bit_length = a1

            def __new_node(self):
                self.__nodes.append([-1] * 2)
                self.__cnts.append(0)
                return len(self.__nodes) - 1

            def update(self, a1, a2):
                v1 = 0
                for v2 in reversed(range(self.__bit_length)):
                    v3 = a1 >> v2
                    if self.__nodes[v1][v3 & 1] == -1:
                        self.__nodes[v1][v3 & 1] = self.__new_node()
                    v1 = self.__nodes[v1][v3 & 1]
                    self.__cnts[v1] += a2

            def query(self, a1):
                v1 = v2 = 0
                for v3 in reversed(range(self.__bit_length)):
                    v1 <<= 1
                    v4 = a1 >> v3
                    if self.__nodes[v2][1 ^ v4 & 1] != -1 and self.__cnts[self.__nodes[v2][1 ^ v4 & 1]]:
                        v2 = self.__nodes[v2][1 ^ v4 & 1]
                        v1 |= 1
                    else:
                        v2 = self.__nodes[v2][v4 & 1]
                return v1
        a1.sort()
        v1 = Trie(a1[-1].bit_length())
        v2 = v3 = 0
        for v4, v5 in enumerate(a1):
            v1.update(v5, +1)
            while not a1[v4] <= 2 * a1[v3]:
                v1.update(a1[v3], -1)
                v3 += 1
            v2 = max(v2, v1.query(v5))
        return v2
