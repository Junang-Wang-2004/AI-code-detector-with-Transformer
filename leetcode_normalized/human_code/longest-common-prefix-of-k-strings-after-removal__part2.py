class C1(object):

    def longestCommonPrefix(self, a1, a2):
        """
        """

        class Trie(object):

            def __init__(self):
                self.__root = self.__new_node()

            def __new_node(self):
                return {'cnt': 0, 'max': 0}

            def update(self, a1, a2, a3):
                v1 = [None] * (len(a1) + 1)
                v1[0] = v2 = self.__root
                for v3, v4 in enumerate(a1, 1):
                    if v4 not in v2:
                        v2[v4] = self.__new_node()
                    v1[v3] = v2 = v2[v4]
                for v3 in reversed(range(len(v1))):
                    v2 = v1[v3]
                    v2['cnt'] += a2
                    v2['max'] = v3 if v2['cnt'] >= a3 else 0
                    for v4 in v2.keys():
                        if len(v4) == 1:
                            v2['max'] = max(v2['max'], v2[v4]['max'])

            def query(self):
                return self.__root['max']
        v1 = Trie()
        for v2 in a1:
            v1.update(v2, +1, a2)
        v3 = [0] * len(a1)
        for v4 in range(len(a1)):
            v1.update(a1[v4], -1, a2)
            v3[v4] = v1.query()
            v1.update(a1[v4], +1, a2)
        return v3
