class C1(object):

    def phonePrefix(self, a1):
        """
        """

        class Trie(object):

            def __init__(self):
                self.__nodes = []
                self.__new_node()

            def __new_node(self):
                self.__nodes.append([-1] * (10 + 1))
                return len(self.__nodes) - 1

            def add(self, a1):
                v1 = False
                v2 = 0
                for v3 in range(len(a1)):
                    v4 = ord(a1[v3]) - ord('0')
                    if self.__nodes[v2][v4] == -1:
                        self.__nodes[v2][v4] = self.__new_node()
                        v1 = True
                    elif self.__nodes[self.__nodes[v2][v4]][-1] == True:
                        return False
                    v2 = self.__nodes[v2][v4]
                self.__nodes[v2][-1] = True
                return v1
        v1 = Trie()
        return all((v1.add(x) for v2 in a1))
