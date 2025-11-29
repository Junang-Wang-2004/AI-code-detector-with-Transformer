class Node:
    def __init__(self):
        self.children = {}
        self.indices = []

class PrefixTrie:
    def __init__(self):
        self.root = Node()

    def insert(self, seq, idx):
        curr = self.root
        curr.indices.append(idx)
        for char in seq:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
            curr.indices.append(idx)

    def collect(self, seq):
        curr = self.root
        for char in seq:
            if char not in curr.children:
                return []
            curr = curr.children[char]
        return curr.indices

class WordFilter:
    def __init__(self, words):
        self.pt = PrefixTrie()
        self.st = PrefixTrie()
        n = len(words)
        for k in range(n - 1, -1, -1):
            self.pt.insert(words[k], k)
            self.st.insert(words[k][::-1], k)

    def f(self, pref, suf):
        lefts = self.pt.collect(pref)
        rights = self.st.collect(suf[::-1])
        a, b = 0, 0
        while a < len(lefts) and b < len(rights):
            if lefts[a] == rights[b]:
                return lefts[a]
            elif lefts[a] > rights[b]:
                a += 1
            else:
                b += 1
        return -1
