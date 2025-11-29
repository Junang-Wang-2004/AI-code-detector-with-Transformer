class C1:

    def __init__(self):
        self.children = {}
        self.terminal_value = 0
        self.subtree_sum = 0

class C2:

    def __init__(self):
        self.root_node = C1()

    def insert(self, a1, a2):
        v1 = self.root_node
        v2 = [v1]
        for v3 in a1:
            if v3 not in v1.children:
                v1.children[v3] = C1()
            v1 = v1.children[v3]
            v2.append(v1)
        v4 = a2 - v1.terminal_value
        v1.terminal_value = a2
        for v5 in v2:
            v5.subtree_sum += v4

    def sum(self, a1):
        v1 = self.root_node
        for v2 in a1:
            if v2 not in v1.children:
                return 0
            v1 = v1.children[v2]
        return v1.subtree_sum
