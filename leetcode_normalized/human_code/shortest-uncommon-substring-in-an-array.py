class C1(object):

    def shortestSubstrings(self, a1):
        """
        """

        class Trie(object):

            def __init__(self):
                self.__nodes = []
                self.__cnts = []
                self.__new_node()

            def __new_node(self):
                self.__nodes.append([-1] * 26)
                self.__cnts.append(0)
                return len(self.__nodes) - 1

            def add(self, a1, a2):
                for v1 in range(len(a1)):
                    v2 = 0
                    for v3 in range(v1, len(a1)):
                        v4 = ord(a1[v3]) - ord('a')
                        if self.__nodes[v2][v4] == -1:
                            self.__nodes[v2][v4] = self.__new_node()
                        v2 = self.__nodes[v2][v4]
                        self.__cnts[v2] += a2

            def query(self, a1):
                v1 = (float('inf'), '')
                for v2 in range(len(a1)):
                    v3 = 0
                    for v4 in range(v2, len(a1)):
                        v3 = self.__nodes[v3][ord(a1[v4]) - ord('a')]
                        if self.__cnts[v3] == 0:
                            v1 = min(v1, (v4 - v2 + 1, a1[v2:v4 + 1]))
                            break
                return v1[1]
        v1 = Trie()
        for v2 in a1:
            v1.add(v2, +1)
        v3 = []
        for v2 in a1:
            v1.add(v2, -1)
            v3.append(v1.query(v2))
            v1.add(v2, +1)
        return v3
