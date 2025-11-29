import collections

class C1:

    def __init__(self):
        self.children = {}
        self.candidates = []

    def update(self, a1, a2):
        for v1, (v2, v3) in enumerate(self.candidates):
            if v3 == a1:
                self.candidates[v1] = (-a2, a1)
                break
        else:
            self.candidates.append((-a2, a1))
        self.candidates.sort()
        self.candidates = self.candidates[:3]

    def insert(self, a1, a2):
        v1 = self
        v1.update(a1, a2)
        for v2 in a1:
            if v2 not in v1.children:
                v1.children[v2] = C1()
            v1 = v1.children[v2]
            v1.update(a1, a2)

class C2:

    def __init__(self, a1, a2):
        self.root = C1()
        self.counts = collections.Counter()
        self.curr_node = self.root
        self.typed = []
        for v1, v2 in zip(a1, a2):
            self.counts[v1] = v2
            self.root.insert(v1, v2)

    def input(self, a1):
        if a1 == '#':
            v1 = ''.join(self.typed)
            self.counts[v1] += 1
            self.root.insert(v1, self.counts[v1])
            self.curr_node = self.root
            self.typed.clear()
            return []
        self.typed.append(a1)
        if self.curr_node is None:
            return []
        if a1 not in self.curr_node.children:
            self.curr_node = None
            return []
        self.curr_node = self.curr_node.children[a1]
        return [s for v2, v3 in self.curr_node.candidates]
