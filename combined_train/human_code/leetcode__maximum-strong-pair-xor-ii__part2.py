class C1(object):

    def maximumStrongPairXor(self, a1):
        """
        """

        class Trie(object):

            def __init__(self, a1):
                self.__nodes = []
                self.__mins = []
                self.__maxs = []
                self.__new_node()
                self.__bit_length = a1

            def __new_node(self):
                self.__nodes.append([-1] * 2)
                self.__mins.append(float('inf'))
                self.__maxs.append(float('-inf'))
                return len(self.__nodes) - 1

            def insert(self, a1):
                v1 = 0
                for v2 in reversed(range(self.__bit_length)):
                    v3 = a1 >> v2
                    if self.__nodes[v1][v3 & 1] == -1:
                        self.__nodes[v1][v3 & 1] = self.__new_node()
                    v1 = self.__nodes[v1][v3 & 1]
                    self.__mins[v1] = min(self.__mins[v1], a1)
                    self.__maxs[v1] = max(self.__maxs[v1], a1)

            def query(self, a1):
                v1 = v2 = 0
                for v3 in reversed(range(self.__bit_length)):
                    v1 <<= 1
                    v4 = a1 >> v3
                    v5 = (v1 | 1) ^ v4
                    assert v4 != v5
                    if self.__nodes[v2][v5 & 1] != -1 and (v4 > v5 and a1 <= 2 * self.__maxs[self.__nodes[v2][v5 & 1]] or (v4 < v5 and self.__mins[self.__nodes[v2][v5 & 1]] <= 2 * a1)):
                        v1 |= 1
                        v2 = self.__nodes[v2][v5 & 1]
                    else:
                        v2 = self.__nodes[v2][1 ^ v5 & 1]
                return v1
        v1 = Trie(max(a1).bit_length())
        v2 = 0
        for v3 in a1:
            v1.insert(v3)
            v2 = max(v2, v1.query(v3))
        return v2
