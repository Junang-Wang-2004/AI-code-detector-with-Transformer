class C1:

    def findMaximumXOR(self, a1):
        if not a1:
            return 0
        v1 = max((n.bit_length() for v2 in a1))

        class Node:

            def __init__(self):
                self.children = [None] * 2
        v3 = Node()

        def insert(a1):
            v1 = v3
            for v2 in range(v1 - 1, -1, -1):
                v3 = a1 >> v2 & 1
                if v1.children[v3] is None:
                    v1.children[v3] = Node()
                v1 = v1.children[v3]

        def search(a1):
            v1 = v3
            v2 = 0
            for v3 in range(v1 - 1, -1, -1):
                v4 = a1 >> v3 & 1
                v5 = 1 - v4
                if v1.children[v5]:
                    v2 |= 1 << v3
                    v1 = v1.children[v5]
                elif v1.children[v4]:
                    v1 = v1.children[v4]
                else:
                    return 0
            return v2
        v4 = 0
        for v5 in a1:
            v4 = max(v4, search(v5))
            insert(v5)
        return v4
