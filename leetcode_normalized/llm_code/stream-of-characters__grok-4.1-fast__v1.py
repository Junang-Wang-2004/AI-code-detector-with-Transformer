from collections import deque

class C1:

    def __init__(self):
        self.kids = [None] * 26
        self.fail = None
        self.match = False
        self.end = False

class C2:

    def __init__(self, a1):
        self.root = C1()
        self.root.fail = self.root
        self.root.match = False
        for v1 in a1:
            v2 = self.root
            for v3 in v1:
                v4 = ord(v3) - ord('a')
                if v2.kids[v4] is None:
                    v2.kids[v4] = C1()
                v2 = v2.kids[v4]
            v2.end = True
        v5 = deque()
        for v4 in range(26):
            if self.root.kids[v4] is not None:
                v6 = self.root.kids[v4]
                v6.fail = self.root
                v6.match = v6.end or self.root.match
                v5.append(v6)
        while v5:
            v2 = v5.popleft()
            for v4 in range(26):
                if v2.kids[v4] is not None:
                    v7 = v2.kids[v4]
                    v8 = v2.fail
                    while v8 != self.root and v8.kids[v4] is None:
                        v8 = v8.fail
                    v9 = v8.kids[v4] if v8.kids[v4] is not None else self.root
                    v7.fail = v9
                    v7.match = v7.end or v9.match
                    v5.append(v7)
        self.node = self.root

    def query(self, a1):
        v1 = ord(a1) - ord('a')
        v2 = self.node
        while v2 != self.root and v2.kids[v1] is None:
            v2 = v2.fail
        v3 = v2.kids[v1] if v2.kids[v1] is not None else self.root
        self.node = v3
        return self.node.match
