class C1:

    def at(self, a1):
        pass

    def size(self):
        pass

class C2(object):

    def countBlocks(self, a1):
        """
        """

        def binary_search_right(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if not a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a2
        v1 = a1.size()
        v2 = v3 = 0
        while v3 != v1:
            v4 = a1.at(v3)
            v3 = binary_search_right(v3, v1 - 1, lambda x: a1.at(x) == v4) + 1
            v2 += 1
        return v2
