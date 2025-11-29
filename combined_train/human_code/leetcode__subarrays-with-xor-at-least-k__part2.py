class C1(object):

    def countXorSubarrays(self, a1, a2):
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

            def add(self, a1):
                v1 = 0
                for v2 in reversed(range(self.__bit_length)):
                    v3 = a1 >> v2 & 1
                    if self.__nodes[v1][v3] == -1:
                        self.__nodes[v1][v3] = self.__new_node()
                    v1 = self.__nodes[v1][v3]
                    self.__cnts[v1] += 1

            def query(self, a1, a2):
                v1 = v2 = 0
                for v3 in reversed(range(self.__bit_length)):
                    v4 = a2 >> v3 & 1
                    v5 = a1 >> v3 & 1
                    if v4 == 0:
                        v6 = self.__nodes[v2][1 ^ v5]
                        if v6 != -1:
                            v1 += self.__cnts[v6]
                    v2 = self.__nodes[v2][v4 ^ v5]
                    if v2 == -1:
                        break
                else:
                    v1 += self.__cnts[v2]
                return v1
        v1 = v2 = 0
        v3 = max(max(a1), a2, 1)
        v4 = Trie(v3.bit_length())
        v4.add(v2)
        for v5 in a1:
            v2 ^= v5
            v1 += v4.query(v2, a2)
            v4.add(v2)
        return v1
