class C1:

    def phonePrefix(self, a1):

        class TrieNode:

            def __init__(self):
                self.children = {}
                self.is_end = False
        v1 = TrieNode()

        def insert(a1):
            v1 = v1
            for v2 in a1:
                if v1.is_end:
                    return False
                v3 = int(v2)
                if v3 not in v1.children:
                    v1.children[v3] = TrieNode()
                v1 = v1.children[v3]
            if v1.is_end or v1.children:
                return False
            v1.is_end = True
            return True
        for v2 in a1:
            if not insert(v2):
                return False
        return True
