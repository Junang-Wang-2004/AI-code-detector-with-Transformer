from collections import deque

class TrieNode:
    def __init__(self):
        self.kids = [None] * 26
        self.fail = None
        self.match = False
        self.end = False

class StreamChecker:
    def __init__(self, words):
        self.root = TrieNode()
        self.root.fail = self.root
        self.root.match = False
        for word in words:
            cur = self.root
            for char in word:
                i = ord(char) - ord('a')
                if cur.kids[i] is None:
                    cur.kids[i] = TrieNode()
                cur = cur.kids[i]
            cur.end = True
        q = deque()
        for i in range(26):
            if self.root.kids[i] is not None:
                child = self.root.kids[i]
                child.fail = self.root
                child.match = child.end or self.root.match
                q.append(child)
        while q:
            cur = q.popleft()
            for i in range(26):
                if cur.kids[i] is not None:
                    chld = cur.kids[i]
                    f = cur.fail
                    while f != self.root and f.kids[i] is None:
                        f = f.fail
                    fch = f.kids[i] if f.kids[i] is not None else self.root
                    chld.fail = fch
                    chld.match = chld.end or fch.match
                    q.append(chld)
        self.node = self.root

    def query(self, letter):
        i = ord(letter) - ord('a')
        cur = self.node
        while cur != self.root and cur.kids[i] is None:
            cur = cur.fail
        nxt = cur.kids[i] if cur.kids[i] is not None else self.root
        self.node = nxt
        return self.node.match
