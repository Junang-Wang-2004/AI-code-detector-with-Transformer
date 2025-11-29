import functools

class C1(object):

    def __init__(self, a1, a2):
        """
        initialize your data structure here.
        """
        v1 = len(a1)
        self.__original_length = v1
        self.__tree_length = 2 ** (v1.bit_length() + (v1 & v1 - 1 != 0)) - 1
        self.__tree = [-1 for v2 in range(self.__tree_length)]
        self.__count = a2
        self.__constructTree(a1, 0, self.__original_length - 1, 0)

    def query(self, a1, a2):
        return self.__queryRange(a1, a2, 0, self.__original_length - 1, 0)

    def __constructTree(self, a1, a2, a3, a4):
        if a2 > a3:
            return
        if a2 == a3:
            self.__tree[a4] = a1[a2]
            return
        v1 = a2 + (a3 - a2) // 2
        self.__constructTree(a1, a2, v1, a4 * 2 + 1)
        self.__constructTree(a1, v1 + 1, a3, a4 * 2 + 2)
        if self.__tree[a4 * 2 + 1] != -1 and self.__count(self.__tree[a4 * 2 + 1], a2, a3) * 2 > a3 - a2 + 1:
            self.__tree[a4] = self.__tree[a4 * 2 + 1]
        elif self.__tree[a4 * 2 + 2] != -1 and self.__count(self.__tree[a4 * 2 + 2], a2, a3) * 2 > a3 - a2 + 1:
            self.__tree[a4] = self.__tree[a4 * 2 + 2]

    def __queryRange(self, a1, a2, a3, a4, a5):
        if a3 > a4:
            return (-1, -1)
        if a4 < a1 or a3 > a2:
            return (-1, -1)
        if a1 <= a3 and a4 <= a2:
            if self.__tree[a5] != -1:
                v1 = self.__count(self.__tree[a5], a1, a2)
                if v1 * 2 > a2 - a1 + 1:
                    return (self.__tree[a5], v1)
        else:
            v2 = a3 + (a4 - a3) // 2
            v3 = self.__queryRange(a1, a2, a3, v2, a5 * 2 + 1)
            if v3[0] != -1:
                return v3
            v3 = self.__queryRange(a1, a2, v2 + 1, a4, a5 * 2 + 2)
            if v3[0] != -1:
                return v3
        return (-1, -1)

class C2(object):

    def __init__(self, a1):
        """
        """

        def count(a1, a2, a3, a4):
            return bisect.bisect_right(a1[a2], a4) - bisect.bisect_left(a1[a2], a3)
        self.__arr = a1
        self.__inv_idx = collections.defaultdict(list)
        for v1, v2 in enumerate(self.__arr):
            self.__inv_idx[v2].append(v1)
        self.__segment_tree = C1(a1, functools.partial(count, self.__inv_idx))

    def query(self, a1, a2, a3):
        """
        """
        v1 = self.__segment_tree.query(a1, a2)
        if v1[1] >= a3:
            return v1[0]
        return -1
