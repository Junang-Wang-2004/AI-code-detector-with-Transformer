class C1(object):

    def __init__(self, a1, a2=lambda x, y: x + y, a3=lambda x, y: y, a4=0):
        """
        initialize your data structure here.
        """
        v1 = len(a1)
        self.__original_length = v1
        self.__tree_length = 2 ** (v1.bit_length() + (v1 & v1 - 1 != 0)) - 1
        self.__query_fn = a2
        self.__update_fn = a3
        self.__default_val = a4
        self.__tree = [a4 for v2 in range(self.__tree_length)]
        self.__lazy = [None for v2 in range(self.__tree_length)]
        self.__constructTree(a1, 0, self.__original_length - 1, 0)

    def update(self, a1, a2):
        self.__updateTree(a2, a1, a1, 0, self.__original_length - 1, 0)

    def sumRange(self, a1, a2):
        return self.__queryRange(a1, a2, 0, self.__original_length - 1, 0)

    def __constructTree(self, a1, a2, a3, a4):
        if a2 > a3:
            return
        if a2 == a3:
            self.__tree[a4] = self.__update_fn(self.__tree[a4], a1[a2])
            return
        v1 = a2 + (a3 - a2) // 2
        self.__constructTree(a1, a2, v1, a4 * 2 + 1)
        self.__constructTree(a1, v1 + 1, a3, a4 * 2 + 2)
        self.__tree[a4] = self.__query_fn(self.__tree[a4 * 2 + 1], self.__tree[a4 * 2 + 2])

    def __apply(self, a1, a2, a3, a4):
        self.__tree[a3] = self.__update_fn(self.__tree[a3], a4)
        if a1 != a2:
            self.__lazy[a3 * 2 + 1] = self.__update_fn(self.__lazy[a3 * 2 + 1], a4)
            self.__lazy[a3 * 2 + 2] = self.__update_fn(self.__lazy[a3 * 2 + 2], a4)

    def __updateTree(self, a1, a2, a3, a4, a5, a6):
        if a4 > a5:
            return
        if self.__lazy[a6] is not None:
            self.__apply(a4, a5, a6, self.__lazy[a6])
            self.__lazy[a6] = None
        if a2 > a5 or a3 < a4:
            return
        if a2 <= a4 and a5 <= a3:
            self.__apply(a4, a5, a6, a1)
            return
        v1 = a4 + (a5 - a4) // 2
        self.__updateTree(a1, a2, a3, a4, v1, a6 * 2 + 1)
        self.__updateTree(a1, a2, a3, v1 + 1, a5, a6 * 2 + 2)
        self.__tree[a6] = self.__query_fn(self.__tree[a6 * 2 + 1], self.__tree[a6 * 2 + 2])

    def __queryRange(self, a1, a2, a3, a4, a5):
        if a3 > a4:
            return self.__default_val
        if self.__lazy[a5] is not None:
            self.__apply(a3, a4, a5, self.__lazy[a5])
            self.__lazy[a5] = None
        if a4 < a1 or a3 > a2:
            return self.__default_val
        if a1 <= a3 and a4 <= a2:
            return self.__tree[a5]
        v1 = a3 + (a4 - a3) // 2
        return self.__query_fn(self.__queryRange(a1, a2, a3, v1, a5 * 2 + 1), self.__queryRange(a1, a2, v1 + 1, a4, a5 * 2 + 2))
