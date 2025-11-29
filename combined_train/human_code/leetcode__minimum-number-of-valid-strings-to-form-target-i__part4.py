class C1(object):

    def minValidStrings(self, a1, a2):
        """
        """

        class Trie(object):

            def __init__(self):
                self.__nodes = []
                self.__new_node()

            def __new_node(self):
                self.__nodes.append([-1] * 26)
                return len(self.__nodes) - 1

            def add(self, a1):
                v1 = 0
                for v2 in a1:
                    v3 = ord(v2) - ord('a')
                    if self.__nodes[v1][v3] == -1:
                        self.__nodes[v1][v3] = self.__new_node()
                    v1 = self.__nodes[v1][v3]

            def query(self, a1, a2):
                v1 = 0
                for v2 in range(len(a1) - a2):
                    v3 = ord(a1[a2 + v2]) - ord('a')
                    if self.__nodes[v1][v3] == -1:
                        return v2
                    v1 = self.__nodes[v1][v3]
                return len(a1) - a2
        v1 = Trie()
        for v2 in a1:
            v1.add(v2)
        v3 = [0] * len(a2)
        for v4 in range(len(a2)):
            v5 = v1.query(a2, v4)
            for v6 in range(1, v5 + 1):
                v3[v4 + v6 - 1] = max(v3[v4 + v6 - 1], v6)
        v7 = [0] * (len(a2) + 1)
        for v4 in range(len(a2)):
            if not v3[v4]:
                return -1
            v7[v4 + 1] = v7[v4 - v3[v4] + 1] + 1
        return v7[-1]
