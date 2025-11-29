class C1(object):

    def longestCommonPrefix(self, a1, a2):
        """
        """

        class Trie(object):

            def __init__(self):
                self.__nodes = []
                self.__cnt = []
                self.__mx = []
                self.__new_node()

            def __new_node(self):
                self.__nodes.append([-1] * 26)
                self.__cnt.append(0)
                self.__mx.append(0)
                return len(self.__nodes) - 1

            def update(self, a1, a2, a3):
                v1 = [-1] * (len(a1) + 1)
                v1[0] = v2 = 0
                for v3, v4 in enumerate(a1, 1):
                    v5 = ord(v4) - ord('a')
                    if self.__nodes[v2][v5] == -1:
                        self.__nodes[v2][v5] = self.__new_node()
                    v1[v3] = v2 = self.__nodes[v2][v5]
                for v3 in reversed(range(len(v1))):
                    v2 = v1[v3]
                    self.__cnt[v2] += a2
                    self.__mx[v2] = v3 if self.__cnt[v2] >= a3 else 0
                    for v5 in range(len(self.__nodes[v2])):
                        if self.__nodes[v2][v5] != -1:
                            self.__mx[v2] = max(self.__mx[v2], self.__mx[self.__nodes[v2][v5]])

            def query(self):
                return self.__mx[0]
        v1 = [0] * len(a1)
        v2 = Trie()
        for v3 in a1:
            v2.update(v3, +1, a2)
        for v4 in range(len(a1)):
            v2.update(a1[v4], -1, a2)
            v1[v4] = v2.query()
            v2.update(a1[v4], +1, a2)
        return v1
