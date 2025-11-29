class C1(object):

    def stringIndices(self, a1, a2):
        """
        """
        v1 = float('INF')

        class Trie(object):

            def __init__(self):
                self.__nodes = []
                self.__mns = []
                self.__new_node()

            def __new_node(self):
                self.__nodes.append([-1] * 26)
                self.__mns.append((v1, v1))
                return len(self.__nodes) - 1

            def add(self, a1, a2):
                v1 = 0
                self.__mns[v1] = min(self.__mns[v1], (len(a2), a1))
                for v2 in reversed(a2):
                    v3 = ord(v2) - ord('a')
                    if self.__nodes[v1][v3] == -1:
                        self.__nodes[v1][v3] = self.__new_node()
                    v1 = self.__nodes[v1][v3]
                    self.__mns[v1] = min(self.__mns[v1], (len(a2), a1))

            def query(self, a1):
                v1 = 0
                for v2 in reversed(a1):
                    v3 = ord(v2) - ord('a')
                    if self.__nodes[v1][v3] == -1:
                        break
                    v1 = self.__nodes[v1][v3]
                return self.__mns[v1][1]
        v2 = Trie()
        for v3, v4 in enumerate(a1):
            v2.add(v3, v4)
        return [v2.query(v4) for v4 in a2]
