import collections

class C1:

    def __init__(self):
        self.children = {}
        self.failure = None
        self.word_ids = []
        self.match_ids = []

class C2:

    def __init__(self, a1):
        self.root = C1()
        self.populate_trie(a1)
        self.setup_failures()

    def populate_trie(self, a1):
        for v1, v2 in enumerate(a1):
            v3 = self.root
            for v4 in v2:
                if v4 not in v3.children:
                    v3.children[v4] = C1()
                v3 = v3.children[v4]
            v3.word_ids.append(v1)

    def setup_failures(self):
        v1 = collections.deque()
        self.root.failure = self.root
        self.root.match_ids = []
        for v2 in list(self.root.children.values()):
            v2.failure = self.root
            v1.append(v2)
        while v1:
            v3 = v1.popleft()
            v3.match_ids = v3.word_ids[:] + v3.failure.match_ids
            for v4, v2 in v3.children.items():
                v5 = v3.failure
                while v5 != self.root and v4 not in v5.children:
                    v5 = v5.failure
                v2.failure = v5.children.get(v4, self.root)
                v1.append(v2)

class C3:

    def indexPairs(self, a1, a2):
        if not a2:
            return []
        v1 = C2(a2)
        v2 = []
        v3 = v1.root
        for v4 in range(len(a1)):
            v5 = a1[v4]
            while v3 != v1.root and v5 not in v3.children:
                v3 = v3.failure
            v3 = v3.children.get(v5, v1.root)
            for v6 in v3.match_ids:
                v7 = len(a2[v6])
                v8 = v4 - v7 + 1
                v2.append([v8, v4])
        return sorted(v2)
