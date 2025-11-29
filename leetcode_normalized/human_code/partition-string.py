class C1(object):

    def partitionString(self, a1):
        """
        """

        class Trie(object):

            def __init__(self):
                self.__nodes = []
                self.__new_node()
                self.__curr = 0

            def __new_node(self):
                self.__nodes.append([-1] * 26)
                return len(self.__nodes) - 1

            def add(self, a1):
                v1 = ord(a1) - ord('a')
                if self.__nodes[self.__curr][v1] == -1:
                    self.__nodes[self.__curr][v1] = self.__new_node()
                    self.__curr = 0
                    return
                self.__curr = self.__nodes[self.__curr][v1]

            def curr(self):
                return self.__curr
        v1 = []
        v2 = Trie()
        v3 = []
        for v4 in a1:
            v3.append(v4)
            v2.add(v4)
            if v2.curr():
                continue
            v1.append(''.join(v3))
            v3 = []
        return v1
