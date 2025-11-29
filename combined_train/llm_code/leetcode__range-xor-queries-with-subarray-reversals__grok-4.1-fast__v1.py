import random

class C1:

    class Node:

        def __init__(self, a1):
            self.val = a1
            self.prio = random.randrange(1 << 31)
            self.sz = 1
            self.xsum = a1
            self.flip = False
            self.lc = None
            self.rc = None

    def __init__(self, a1):
        self.root = self._build(a1, 0, len(a1))

    def _build(self, a1, a2, a3):
        if a2 == a3:
            return None
        v1 = (a2 + a3) // 2
        v2 = self.Node(a1[v1])
        v2.lc = self._build(a1, a2, v1)
        v2.rc = self._build(a1, v1 + 1, a3)
        self._update_node(v2)
        return v2

    def _get_size(self, a1):
        return a1.sz if a1 else 0

    def _get_xor(self, a1):
        return a1.xsum if a1 else 0

    def _push(self, a1):
        if not a1 or not a1.flip:
            return
        a1.flip = False
        a1.lc, a1.rc = (a1.rc, a1.lc)
        if a1.lc:
            a1.lc.flip = not a1.lc.flip
        if a1.rc:
            a1.rc.flip = not a1.rc.flip

    def _update_node(self, a1):
        if a1:
            a1.sz = 1 + self._get_size(a1.lc) + self._get_size(a1.rc)
            a1.xsum = a1.val ^ self._get_xor(a1.lc) ^ self._get_xor(a1.rc)

    def _split(self, a1, a2):
        if a1 is None:
            return (None, None)
        self._push(a1)
        v1 = self._get_size(a1.lc)
        if v1 >= a2:
            v2, a1.lc = self._split(a1.lc, a2)
            self._update_node(a1)
            return (v2, a1)
        else:
            a1.rc, v3 = self._split(a1.rc, a2 - v1 - 1)
            self._update_node(a1)
            return (a1, v3)

    def _merge(self, a1, a2):
        self._push(a1)
        self._push(a2)
        if a1 is None:
            return a2
        if a2 is None:
            return a1
        if a1.prio > a2.prio:
            a1.rc = self._merge(a1.rc, a2)
            self._update_node(a1)
            return a1
        a2.lc = self._merge(a1, a2.lc)
        self._update_node(a2)
        return a2

    def update(self, a1, a2):
        v1, v2 = self._split(self.root, a1 - 1)
        v2, v3 = self._split(v2, 1)
        if v2:
            v2.val = a2
            self._update_node(v2)
        self.root = self._merge(self._merge(v1, v2), v3)

    def query(self, a1, a2):
        v1, v2 = self._split(self.root, a1 - 1)
        v2, v3 = self._split(v2, a2 - a1 + 1)
        v4 = self._get_xor(v2)
        self.root = self._merge(self._merge(v1, v2), v3)
        return v4

    def reverse(self, a1, a2):
        v1, v2 = self._split(self.root, a1 - 1)
        v2, v3 = self._split(v2, a2 - a1 + 1)
        if v2:
            v2.flip = not v2.flip
        self.root = self._merge(self._merge(v1, v2), v3)

class C3:

    def getResults(self, a1, a2):
        v1 = C1(a1)
        v2 = []
        for v3 in a2:
            v4, v5, v6 = v3
            if v4 == 1:
                v1.update(v5, v6)
            elif v4 == 2:
                v2.append(v1.query(v5, v6))
            elif v4 == 3:
                v1.reverse(v5, v6)
        return v2
